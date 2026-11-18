#### [Feb 1, 2023 General — Q1] · [Feb 1, 2023 2nd Partial — Q1] (6 points, open question)
**Question.** State the Black–Scholes Partial Differential Equation and the terminal condition at maturity for a European call option in the Black–Scholes market.

**Answer.** The NA price of the call is $c(t)=F(t,S(t))$ where $F$ solves, for all $0<t<T$ and $x>0$,
$$\frac{\partial F}{\partial t}(t,x)+rx\frac{\partial F}{\partial x}(t,x)+\frac12\sigma^2x^2\frac{\partial^2F}{\partial x^2}(t,x)=rF(t,x),$$
with terminal condition $F(T,x)=(x-K)^+$ for all $x>0$.

#### [Jan 31, 2022 General — Question 2] (6 points, mark all the appropriate answers)
**Question.** Let $\pi$ be the *hedging portfolio* in the derivation of the Black–Scholes PDE for a European derivative. The portfolio $\pi$…

- **A.** involves positions on the riskless asset $B$ and the risky asset $S$
- **B.** involves positions on the European derivative and the risky asset $S$
- **C.** is self-financing
- **D.** is locally riskless

**Correct answers: B, C, D.** $\pi=hS-F$: short one derivative and $h=F_S$ shares; it is self-financing; with the delta hedge the $dW^P$ term vanishes, so it is locally riskless. It contains **no** bond (that is the *replicating* strategy of Prop. 184).

#### [Feb 1, 2023 General — Q2] · [Feb 1, 2023 2nd Partial — Q2] (4 points)
**Question.** Let $\pi(t)$ be the hedging portfolio in the derivation of the Black–Scholes PDE for a European derivative. The portfolio $\pi$…

- **A.** involves positions on the riskless asset $B$ and the risky asset $S$
- **B.** involves a buy-and-hold position on the European derivative
- **C.** is self-financing and locally riskless
- **D.** involves a buy-and-hold position on the risky asset $S$ that makes $\pi$ locally riskless

**Correct answer: C** (official solution: full marks for **B and C** together, or C alone — the portfolio is constantly short one unit of the derivative). A is false (no bond); D is false: the stock position $h(t)=F_S(t,S(t))$ is continuously **rebalanced**.

#### [Jan 2024 1st exam — Question 3] (4 points, mark all the appropriate answers)
**Question.** Let $\pi$ be the hedging portfolio in the derivation of the Black–Scholes PDE for a European derivative. The portfolio $\pi$…

- **A.** coincides with the replicating strategy of the European derivative
- **B.** involves positions on the European derivative and the risky asset $S$
- **C.** is always long on the European derivative
- **D.** is locally riskless and self-financing

**Correct answers: B, D.** A is false (the replicating strategy uses $B$ and $S$ and is risky); C is false: it is **short** one derivative.

#### [Jan 13, 2025 — Question 3] (6 points, mark all the appropriate answers)
**Question.** Let $\pi$ be the hedging portfolio in the derivation of the Black–Scholes PDE for a European derivative. The portfolio $\pi$…

- **A.** coincides with the replicating strategy of the European derivative
- **B.** involves positions on the European derivative and the risky asset $S$
- **C.** is always short on the European derivative
- **D.** is buy-and-hold, i.e. it is never rebalanced as $t$ varies in $(0,T)$

**Correct answers: B, C.** D is false: $h(t)=F_S(t,S(t))$ changes continuously (delta hedging = continuous rebalancing).

#### [Dec 19, 2025 — Question 3] (4 points, mark all the appropriate answers)
**Question.** Let $\pi$ be the hedging portfolio in the derivation of the Black–Scholes PDE for a European derivative. The portfolio $\pi$…

- **A.** consists of an investment in the riskless asset $B$
- **B.** is self-financing and locally riskless
- **C.** cannot be locally riskless, because it involves a position on the risky asset $S$
- **D.** requires continuously rebalancing as $t$ varies in $(0,T)$

**Correct answers: B, D.** A is false (no bond); C is false: the delta hedge cancels the risk of $S$ against the risk of the derivative.

#### [Jan 31, 2022 General — Question 3] (4 points, mark all the appropriate alternatives)
**Question.** Consider a European derivative whose final payoff at $T$ is $X(T)$. The no-arbitrage price at $t$ of the European derivative satisfies the Black–Scholes PDE if $X(T)$ is

- **A.** $X(T)=\max(K-S(T);0)$ with $K\in\mathbb{R}$
- **B.** $X(T)=\sqrt{S(T)/S(\frac T2)}$
- **C.** $X(T)=S(T)$
- **D.** $X(T)=\max\big(K-\min_{0\le t\le T}S(t);0\big)$ with $K\in\mathbb{R}$

**Correct answers: A, C.** Prop. 182 requires $X(T)=f(S(T))$, a function of the **terminal** price only. B and D are path-dependent: their price is not a function $F(t,S(t))$ of today's price only.

#### [Jan 29, 2025 — Question 3] (6 points, mark all the appropriate statements)
**Question.** The Black–Scholes PDE for a European derivative with terminal payoff $f(S(T))$ and price $F(t,S(t))$ at $t\in[0,T]$…

- **A.** is verified for all $t\in(0,T)$ and for all possible time-$t$ values of $S$
- **B.** is a no-arbitrage restriction on $F$
- **C.** implies that $F(t,S(t))=F(0,S(0))$ for all $t\in(0,T)$
- **D.** requires $F$ to be continuously differentiable *once* with respect to the *first* argument and *twice* with respect to the *second* argument

**Correct answers: A, B, D.** C is false: the price changes with $t$ and $S$ (only the *discounted* price is a $Q$-martingale).

#### [Jan 16, 2023 General — Q2] · [Jan 16, 2023 2nd Partial — Q2] (4 points, mark the appropriate alternatives)
**Question.** In the Black–Scholes model, the price of a European call option with maturity $T$, strike $K$ at time $t\in(0,T)$ is $c(t)=S(t)N(d_1)-Ke^{-r(T-t)}N(d_2)$, where $N(y)=\int_{-\infty}^y\frac{1}{\sqrt{2\pi}}e^{-z^2/2}dz$, and… (the exam writes $\delta$ for $r$)

- **A.** $d_1=\frac{1}{\sigma\sqrt{T-t}}\Big(\ln\frac{S(t)}{K}+\big(r-\frac12\sigma^2\big)(T-t)\Big)$ and $d_2=d_1+\sigma\sqrt{T-t}$
- **B.** $d_1=\frac{1}{\sigma\sqrt{T-t}}\Big(\ln\frac{S(t)}{K}-\big(r+\frac12\sigma^2\big)(T-t)\Big)$ and $d_2=d_1-\sigma\sqrt{T-t}$
- **C.** $d_1=\frac{1}{\sigma\sqrt{T-t}}\Big(\ln\frac{S(t)}{K}+\big(r-\frac12\sigma^2\big)(T-t)\Big)$ and $d_2=d_1-\sigma\sqrt{T-t}$
- **D.** $d_1=\frac{1}{\sigma\sqrt{T-t}}\Big(\ln\frac{S(t)}{K}+\big(r+\frac12\sigma^2\big)(T-t)\Big)$ and $d_2=d_1-\sigma\sqrt{T-t}$

**Correct answer: D** (Prop. 179). A and C use $-\frac12\sigma^2$ in $d_1$ (that is $d_2$'s numerator); A also has the wrong sign in $d_2$; B subtracts the drift.

#### [Jan 2024 2nd exam — Question 3] (6 points, mark all the appropriate answers)
**Question.** In the formula for the initial price of a European call option on $S$ with maturity $T$ and strike price $K$ in the Black–Scholes model, $c(0)=S(0)N(d_1)-Ke^{-rT}N(d_2)$, where $N$ denotes the standard normal cdf,

- **A.** $d_1=\frac{1}{\sigma\sqrt T}\Big(\ln\frac{S(0)}{K}+\big(r+\frac12\sigma^2\big)T\Big)$ and $d_2=d_1-\sigma\sqrt T$
- **B.** $c(0)\ge0$
- **C.** $N(d_1)=Q[S(T)>K]$
- **D.** $N(d_2)=Q[S(T)>K]$

**Correct answers: A, B, D.** C is false: $N(d_1)$ is the call **delta**; the RN probability of exercise is $N(d_2)$.

#### [Jan 29, 2025 — Question 4] (4 points, mark all appropriate alternatives)
**Question.** In the Black–Scholes model consider a European call option on $S$ with maturity $T$ and strike $K$. Denote with $N$ the standard normal cdf and with $c(0)$ the NA price at $t=0$. Given $d_1=\frac{1}{\sigma\sqrt T}\big(\ln\frac{S(0)}{K}+(r+\frac12\sigma^2)T\big)$ and $d_2=d_1-\sigma\sqrt T$, then

- **A.** $c(0)=S(0)N(d_1)-Ke^{-rT}N(d_2)$
- **B.** $c(0)=S(0)N(d_1)+Ke^{-rT}N(d_2)$
- **C.** $N(d_1)<N(d_2)$
- **D.** $N(d_2)=Q[S(T)>K]$

**Correct answers: A, D.** C is false: $d_1=d_2+\sigma\sqrt T>d_2$, hence $N(d_1)>N(d_2)$.

#### [Jan 2026 — Question 3] (4 points, mark all the appropriate answers)
**Question.** Consider a European derivative in the Black–Scholes market whose final payoff is a deterministic function of the terminal price of the risky stock $S$. Let $F(t,x)$ be the pricing functional of the derivative at time $t$ when the underlying has value $x$. The *replicating strategy* $\vartheta=(\vartheta_0,\vartheta_1)$…

- **A.** consists always of a long position in the riskless asset $B$
- **B.** is self-financing
- **C.** $\vartheta_1(t)=\frac{\partial F(t,S(t))}{\partial x}$
- **D.** is locally riskless

**Correct answers: B, C** (Prop. 184). A is false (replicating a call means borrowing, $\vartheta_0<0$). D is false: it replicates a risky payoff; the locally riskless one is the *hedging portfolio* $\pi$.

#### [Jan 2026 — Question 4] (4 points, mark all appropriate answers)
**Question.** Consider a European put option on $S$ in the Black–Scholes model, with $N$ the standard normal cdf, $d_1=\frac{1}{\sigma\sqrt{T-t}}\big(\ln\frac{S(t)}{K}+(r+\frac12\sigma^2)(T-t)\big)$ and $d_2=d_1-\sigma\sqrt{T-t}$. Denote with $p(t)$ the NA price of the put at $t$ and with $Q$ the risk-neutral probability. Then

- **A.** $p(t)=Ke^{-r(T-t)}N(d_2)-S(t)N(-d_1)$
- **B.** $p(t)=Ke^{-r(T-t)}N(d_2)-S(t)N(d_1)$
- **C.** $p(t)=Ke^{-r(T-t)}N(-d_2)-S(t)N(-d_1)$
- **D.** $Q[S(T)\le K]=N(-d_2)$

**Correct answers: C, D** (Prop. 181; $Q[S(T)\le K]=1-N(d_2)=N(-d_2)$).
