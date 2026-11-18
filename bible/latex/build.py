#!/usr/bin/env python3
"""Build the Quant Finance Bible: md chapters -> LaTeX (pandoc) -> PDF (pdflatex)."""
import os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.dirname(HERE)
CHAPTERS = ["ch00", "ch01", "ch02", "ch03_04", "ch05", "ch07", "ch08", "ch09",
            "ch10", "ch11", "ch14", "ch15", "ch16", "ch99"]

FIG = lambda name, cap: ("\n```{=latex}\n\\begin{figure}[H]\\centering\\input{figs/%s}"
                         "\\caption{%s}\\end{figure}\n```\n" % (name, cap))

# figures inserted after an anchor line (first line that starts with the anchor)
INSERT_AFTER = {
    "ch11": [("### Exercises", FIG("tree_generic", "Information structure used in all two-period exam exercises."))],
    "ch14": [("Processes can have **continuous paths**", FIG("jumps", "Continuous trajectory vs trajectory with jumps (slides, Ch.~14).")),
             ("- Standardization:", FIG("bm_paths", "Three simulated paths of a standard Brownian motion with the $\\pm\\sqrt t$ band.")),
             ("  - Second moment:", FIG("step_beta", "$\\mathbb{E}[(X(T)-X(0))^2]=\\int_0^T\\mathbb{E}[\\beta^2(t)]\\,dt$ is the area below the step function (slides, Ch.~14)."))],
    "ch15": [("- Black–Scholes ⟺ i.i.d. normal", FIG("gbm_paths", "Simulated GBM paths ($S_0=1$, $\\mu=9\\%$, $\\sigma=25\\%$): mean $S_0e^{\\mu t}$ vs median $S_0e^{(\\mu-\\sigma^2/2)t}$."))],
    "ch16": [("**Interpretation:** $N(d_2)", FIG("callprice", "Black--Scholes call price as a function of $S$ for different residual maturities ($K=100$, $r=5\\%$, $\\sigma=20\\%$); it converges to the payoff as $\\tau\\to0$."))],
    "ch03_04": [("8–9. *(2+2) Super-replicating strategy with maximum", FIG("superrep", "Jan 14, 2022 – Exercise 1: super-replication region (above the green envelope) and the minimum-cost super-replicating portfolio."))],
}
# code blocks replaced by TikZ trees
CODE_REPLACE = {
    "ch05": FIG("binom1", "One-period binomial market."),
    "ch07": FIG("infotree", "Event-tree representation of an information structure ($T=3$, $K=7$) from the slides."),
    "ch10": FIG("tree2", "Two-period market where re-trading at $t=1$ completes the market (slides, Ch.~10)."),
}


def preprocess(name, md):
    if name in CODE_REPLACE:
        md = re.sub(r"```\n.*?```\n", lambda m: CODE_REPLACE[name], md, count=1, flags=re.S)
    for anchor, fig in INSERT_AFTER.get(name, []):
        lines = md.split("\n")
        for i, l in enumerate(lines):
            if l.startswith(anchor):
                # insert after the end of this paragraph / list item
                j = i + 1
                while j < len(lines) and lines[j].strip() and not lines[j].startswith(("- ", "#", "> ")) and not re.match(r"^\d+(–\d+)?\. ", lines[j]):
                    j += 1
                lines.insert(j, fig)
                break
        else:
            print("WARNING anchor not found:", name, anchor, file=sys.stderr)
        md = "\n".join(lines)
    # exam boxes: "> ### ★ EXAM — title" -> bold title line inside the quote
    md = re.sub(r"^> ### ★ EXAM — (.*)$", r"> **EXAMBOX \1**", md, flags=re.M)
    md = md.replace("★ EXAM", "EXAM")
    md = re.sub(r"^(\s+)> \*Note:\*", r"\1**Note on the official solution:**", md, flags=re.M)
    # "8–9. text" (combined points) -> "8. text" + "9. (see Point 8)" so list numbering stays right
    md = re.sub(r"^(\d+)–(\d+)\. (.*)$", lambda m: "%s. %s\n%s. *(answered together with Point %s above)*" % (m.group(1), m.group(3), m.group(2), m.group(1)), md, flags=re.M)
    # pandoc needs a blank line before a list that follows a paragraph (also inside quotes)
    lines = md.split("\n"); out = []
    lst = re.compile(r"^(> )?\s*(\d+(–\d+)?\.|[-*]) ")
    for l in lines:
        if out and lst.match(l):
            prev = out[-1]
            q = l.startswith("> ")
            pq = prev.startswith(">")
            pbody = prev[1:].strip() if pq else prev.strip()
            if pbody and not lst.match(prev) and not prev.startswith("  ") and q == pq and not pbody.startswith("#") and not pbody.startswith("|"):
                out.append(">" if q else "")
        if out and re.match(r"^(> )?\|", l) and not re.match(r"^>? ?\|", out[-1]) and out[-1].strip(" >"):
            out.append(">" if l.startswith(">") else "")
        out.append(l)
    return "\n".join(out)


UNICODE = {
    "—": "---", "–": "--", "⇒": r"$\Rightarrow$", "⟺": r"$\Longleftrightarrow$", "⇔": r"$\Leftrightarrow$",
    "⇐": r"$\Leftarrow$", "∃": r"$\exists$", "∀": r"$\forall$", "∎": r"$\blacksquare$", "✓": r"\checkmark{}",
    "≈": r"$\approx$", "−": "-", "×": r"$\times$", "…": r"\ldots{}", "ω": r"$\omega$", "Ω": r"$\Omega$",
    "★": r"$\bigstar$", "§": r"\S{}",
}


def postprocess(tex):
    # quotes -> boxes
    out = []
    parts = re.split(r"(\\begin\{quote\}|\\end\{quote\})", tex)
    i = 0
    while i < len(parts):
        p = parts[i]
        if p == "\\begin{quote}":
            body = parts[i + 1]
            m = re.search(r"\\textbf\{EXAMBOX (.*?)\}\n", body, flags=re.S)
            if m:
                title = m.group(1)
                body = body[:m.start()] + body[m.end():]
                out.append("\\begin{exambox}{%s}" % title + body + "\\end{exambox}")
            else:
                out.append("\\begin{infobox}" + body + "\\end{infobox}")
            i += 3
            continue
        out.append(p)
        i += 1
    tex = "".join(out)
    # unicode outside math (pandoc keeps them verbatim)
    for k, v in UNICODE.items():
        tex = tex.replace(k, v)
    tex = tex.replace("$$\\Rightarrow$$", "$\\Rightarrow$")
    return tex


def md2tex(name):
    md = open(os.path.join(SRC, name + ".md"), encoding="utf-8").read()
    md = preprocess(name, md)
    tmp = os.path.join(HERE, "build", name + ".pre.md")
    open(tmp, "w", encoding="utf-8").write(md)
    res = subprocess.run(["pandoc", tmp, "-f", "markdown-yaml_metadata_block+tex_math_dollars+raw_tex+pipe_tables",
                          "-t", "latex", "--top-level-division=chapter", "--wrap=preserve"],
                         capture_output=True, text=True)
    if res.returncode:
        sys.exit(res.stderr)
    tex = postprocess(res.stdout)
    if name == "ch99":
        tex = "\\appendix\n" + tex
    if name == "ch00":
        tex = tex.replace("\\chapter{", "\\chapter*{", 1)
        tex = tex.replace("\\label{how-to-use-this-bible}", "\\addcontentsline{toc}{chapter}{How to Use This Bible}\\label{how-to-use-this-bible}")
    out = os.path.join(HERE, "build", name + ".tex")
    open(out, "w", encoding="utf-8").write(tex)
    return name + ".tex"


def main():
    os.makedirs(os.path.join(HERE, "build"), exist_ok=True)
    body = "\n".join("\\input{build/%s}" % md2tex(c) for c in CHAPTERS)
    main_tex = open(os.path.join(HERE, "preamble.tex"), encoding="utf-8").read().replace("%%BODY%%", body)
    open(os.path.join(HERE, "QuantBible.tex"), "w", encoding="utf-8").write(main_tex)
    for _ in range(3):
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "QuantBible.tex"],
                           cwd=HERE, capture_output=True, text=True)
        if r.returncode:
            print(r.stdout[-4000:])
            sys.exit("pdflatex failed")
    print("OK")


if __name__ == "__main__":
    main()
