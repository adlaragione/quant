#### [Jan 16, 2023 2nd Partial — Question 1] (6 points, open question)
**Question.** State the First Fundamental Theorem of Asset Pricing in the multiperiod market model.

**Answer.** In a discrete-time multi-period financial market the following are equivalent:
1. the market is arbitrage-free;
2. there exists an equivalent martingale measure (risk-neutral probability) $Q$, i.e. a strictly positive probability on $\Omega$ such that $S_j(t)=\mathbb{E}^Q\big[\frac{S_j(t+1)}{1+r(t)}\,\big|\,\mathcal{P}_t\big]$ for all $j=1,\dots,N$ and $t=0,\dots,T-1$.

(Theorem 111.)

#### [Jan 2024 1st exam — Question 2] (6 points, mark all the appropriate sentences)
**Question.** Let $Q$ denote a risk-neutral probability for an arbitrage-free discrete multiperiod market with assets $B,S_1,\dots,S_N$. Then

- **A.** $Q(\omega_k)>0$ for all $\omega_k\in\Omega$
- **B.** $\{S_j(t)\}_t$ is a $Q$-martingale, for all $j=1,\dots,N$
- **C.** $S_j(t)=\mathbb{E}^Q_t\Big[\frac{S_j(t+1)}{1+r(t)}\,\Big|\,\mathcal{P}_t\Big]$ for all $t=0,\dots,T-1$, for all $j=1,\dots,N$
- **D.** $\{B(t)\}_t$ is a $Q$-martingale

**Correct answers: A, C** (Definition 109).
- B is false: only *discounted* prices $S_j/B$ are martingales (unless $r=0$).
- D is false: $B(t+1)=B(t)(1+r(t))>B(t)$ when $r>0$.

#### [Jan 13, 2025 — Question 2] (2 points)
**Question.** Let $Q$ denote a risk-neutral probability for an arbitrage-free discrete multiperiod market with assets $B,S_1,\dots,S_N$. Then

- **A.** $Q(\omega_k)=0$ for all $\omega_k\in\Omega$
- **B.** $S_j(t)=\mathbb{E}^Q\Big[\frac{S_j(t+1)}{1+r(t+1)}\,\Big|\,\mathcal{P}_t\Big]$ for all $t=0,\dots,T-1$, for all $j$
- **C.** $\{S_j(t)\}_{t=0}^T$ is a $Q$-martingale, for all $j=1,\dots,N$
- **D.** $S_j(t)=\mathbb{E}^Q\Big[\frac{S_j(t+1)}{1+r(t)}\,\Big|\,\mathcal{P}_t\Big]$ for all $t=0,\dots,T-1$, for all $j$

**Correct answer: D.**
- A: $Q$ must be strictly positive.
- B: wrong rate — over $[t,t+1]$ the rate is $r(t)$, known at $t$, not $r(t+1)$.
- C: only discounted prices are martingales.
