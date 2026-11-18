#### [Jan 2024 2nd exam — Question 2] (4 points, mark all the appropriate sentences)
**Question.** Consider the discrete multiperiod market with assets $B,S_1,\dots,S_N$. A self-financing strategy $\vartheta$ satisfies

- **A.** $\vartheta_0(t-1)B(t)+\sum_{j=1}^N\vartheta_j(t-1)S_j(t)=V_\vartheta(t)$, $\quad t=1,\dots,T-1$
- **B.** $\{V_\vartheta(t)\}_t$ is a $Q$-martingale, for any risk-neutral probability $Q$
- **C.** $V_\vartheta(t)=0$, $\quad t=1,\dots,T-1$
- **D.** $C_\vartheta(t)=0$, $\quad t=1,\dots,T-1$

**Correct answers: A, D** (Definition 100 and its equivalent form).
- B is false: the *discounted* value $\tilde V_\vartheta=V_\vartheta/B$ is a $Q$-martingale, not $V_\vartheta$.
- C confuses value and cashflow.

#### [Jan 29, 2025 — Question 2] (4 points, mark all appropriate statements)
**Question.** Consider the discrete multiperiod market with assets $B,S_1,\dots,S_N$. Denote with $\tilde S_1,\dots,\tilde S_N$ their discounted values and with $\tilde V_\vartheta$ the discounted value of a strategy $\vartheta$. Any generic *self-financing* strategy $\vartheta$ then satisfies

- **A.** $\vartheta_0(t-1)+\sum_{j=1}^N\vartheta_j(t-1)\tilde S_j(t)=\tilde V_\vartheta(t)$, $\quad t=1,\dots,T-1$
- **B.** $\tilde V_\vartheta(t)=0$, $\quad t=1,\dots,T-1$
- **C.** $\vartheta_0(t)+\sum_{j=1}^N\vartheta_j(t)\tilde S_j(t)=\tilde V_\vartheta(t)$, $\quad t=0,\dots,T-1$
- **D.** $\tilde V_\vartheta(t)=\tilde V_\vartheta(0)$, $\quad t=1,\dots,T-1$

**Correct answers: A, C.**
- C is the definition of the value divided by $B(t)$ (true for *any* strategy).
- A is the self-financing condition (Def. 100) divided by $B(t)$.
- B and D are false: the value is not zero nor constant (it moves with prices).
