**[Jan 31, 2022 – General, Q2 (6 pts)]** *Let $\pi$ be the hedging portfolio in the derivation of the BS PDE for a European derivative. The portfolio… (mark all)*
A. involves positions on the riskless asset $B$ and the risky asset $S$ — B. involves positions on the European derivative and the risky asset $S$ — C. is self-financing — D. is locally riskless.
**Answer: B, C, D.** $\pi=hS-F$: short one derivative, $h=F_S$ shares; assumed self-financing; with the delta hedge the $dW^P$ term vanishes ⇒ locally riskless. It contains **no** position in $B$ (that is the *replicating* strategy, Prop. 184, not the hedging portfolio).

**[Jan 31, 2022 – General, Q3 (4 pts)]** *The NA price at $t$ of a European derivative with payoff $X(T)$ satisfies the BS PDE if $X(T)$ is (mark all):*
A. $\max(K-S(T),0)$ — B. $S(T)/S(T/2)$ — C. $S(T)$ — D. $\max(K-\min_{0\le t\le T}S(t),0)$.
**Answer: A, C.** Prop. 182 requires $X(T)=f(S(T))$, a function of the **terminal** price only. B and D are path-dependent (their price is not a function $F(t,S(t))$ only).

**[Jan 16, 2023 – General, Q2 (4 pts)]** *BS call price $c(t)=S(t)N(d_1)-Ke^{-r(T-t)}N(d_2)$, where… (options differ in the sign in front of $\frac12\sigma^2$, in using $\mu$ vs $r$, and in $d_2=d_1\pm\sigma\sqrt{T-t}$)*
**Answer: D:** $d_1=\frac{1}{\sigma\sqrt{T-t}}\big[\ln\frac{S(t)}{K}+(r+\frac12\sigma^2)(T-t)\big]$ and $d_2=d_1-\sigma\sqrt{T-t}$. Traps: $\mu$ instead of $r$; $-\frac12\sigma^2$ in $d_1$; $d_2=d_1+\sigma\sqrt{T-t}$.

**[Feb 1, 2023 – General & 2nd Partial, Q1 (6 pts)]** *State the BS PDE and the terminal condition at maturity for a European call option in the BS market.*
**Answer.** The NA price is $c(t)=F(t,S(t))$ where $F$ solves, for $0<t<T$, $x>0$:
$$\frac{\partial F}{\partial t}(t,x)+rx\frac{\partial F}{\partial x}(t,x)+\frac12\sigma^2x^2\frac{\partial^2F}{\partial x^2}(t,x)=rF(t,x),$$
with terminal condition $F(T,x)=(x-K)^+$ for all $x>0$.

**[Feb 1, 2023, Q2 (4 pts)]** *Let $\pi(t)$ be the hedging portfolio in the derivation of the BS PDE. The portfolio…* A. involves positions on $B$ and $S$ — B. involves a buy-and-hold position on the European derivative — C. is self-financing and locally riskless — D. involves a buy-and-hold position on $S$ that makes $\pi$ locally riskless.
**Answer: C** (official: full marks for **B and C** jointly, or C alone — the portfolio is constantly short one unit of the derivative). A is false (no bond); D is false: the stock position $h(t)=F_S(t,S(t))$ is continuously **rebalanced**, not buy-and-hold.

**[Jan 2024 (1st exam), Q3 (4 pts)]** *The hedging portfolio $\pi$ in the derivation of the BS PDE… (mark all)* A. coincides with the replicating strategy of the derivative — B. involves positions on the derivative and on $S$ — C. is always long on the derivative — D. is locally riskless and self-financing.
**Answer: B, D.** A false (replicating strategy uses $B$ and $S$ and is risky); C false: it is **short** one derivative.

**[Jan 2024 (2nd exam), Q3 (6 pts)]** *In $c(0)=S(0)N(d_1)-Ke^{-rT}N(d_2)$ (mark all):* A. $d_1=\frac{1}{\sigma\sqrt T}[\ln\frac{S(0)}K+(r+\frac{\sigma^2}2)T]$ and $d_2=d_1-\sigma\sqrt T$ — B. $c(0)\ge0$ — C. $N(d_1)=Q[S(T)>K]$ — D. $N(d_2)=Q[S(T)>K]$.
**Answer: A, B, D.** C is false: $N(d_1)$ is the call **delta** (and the exercise probability under the measure with the stock as numéraire), while the RN exercise probability is $N(d_2)$.

**[Jan 13, 2025, Q3 (6 pts)]** *Hedging portfolio $\pi$ of the BS PDE derivation… (mark all)* A. coincides with the replicating strategy — B. involves positions on the derivative and on $S$ — C. is always short on the European derivative — D. is buy-and-hold (never rebalanced).
**Answer: B, C.** D false: $h(t)=F_S(t,S(t))$ changes continuously (delta-hedging = continuous rebalancing).

**[Jan 29, 2025, Q3 (6 pts)]** *The BS PDE for a derivative with payoff $f(S(T))$ and price $F(t,S(t))$… (mark all)* A. is verified for all $t\in(0,T)$ and all possible time-$t$ values of $S$ — B. is a no-arbitrage restriction on $F$ — C. implies $F(t,S(t))=F(0,S(0))$ for all $t$ — D. requires $F$ to be $C^1$ in the first argument and $C^2$ in the second.
**Answer: A, B, D.** C is false (the price moves with $t$ and $S$; only the *discounted* price is a $Q$-martingale).

**[Jan 29, 2025, Q4 (4 pts)]** *Given $d_1,d_2$ as usual (mark all):* A. $c(0)=S(0)N(d_1)-Ke^{-rT}N(d_2)$ — B. $c(0)=S(0)N(d_1)+Ke^{-rT}N(d_2)$ — C. $N(d_1)<N(d_2)$ — D. $N(d_2)=Q[S(T)>K]$.
**Answer: A, D.** C is false: $d_1=d_2+\sigma\sqrt T>d_2$ ⇒ $N(d_1)>N(d_2)$.

**[Dec 19, 2025, Q3 (4 pts)]** *The hedging portfolio $\pi$ in the derivation of the BS PDE…* A. consists of an investment in the riskless asset $B$ — B. is self-financing and locally riskless — C. cannot be locally riskless because it involves a position on $S$ — D. requires continuous rebalancing as $t$ varies in $(0,T)$.
**Answer: B, D.**

**[Jan 2026, Q3 (4 pts)]** *Derivative with payoff $f(S(T))$, pricing function $F(t,x)$. The replicating strategy $\vartheta=(\vartheta_0,\vartheta_1)$ (mark all):* A. always has a long position in $B$ — B. is self-financing — C. $\vartheta_1(t)=\frac{\partial F}{\partial x}(t,S(t))$ — D. is locally riskless.
**Answer: B, C** (Prop. 184). A false (a call replication borrows: $\vartheta_0<0$). D false: it replicates a risky payoff (it is the *hedging portfolio* $\pi$ that is locally riskless).

**[Jan 2026, Q4 (4 pts)]** *European put in BS; $N$, $d_1$, $d_2$ as usual. Mark all:* A. $p=Ke^{-r(T-t)}N(d_2)-S N(-d_1)$ — B. $p=Ke^{-r(T-t)}N(d_2)-SN(d_1)$ — C. $p=Ke^{-r(T-t)}N(-d_2)-S(t)N(-d_1)$ — D. $Q[S(T)\le K]=N(-d_2)$.
**Answer: C, D** (Prop. 181; $Q[S(T)\le K]=1-N(d_2)=N(-d_2)$).

