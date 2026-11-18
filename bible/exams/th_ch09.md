**[Jan 16, 2023 – 2nd Partial, Q1 (6 pts)]** *State the First Fundamental Theorem of Asset Pricing in the multiperiod market model.*
**Answer.** In a discrete-time multi-period financial market the following are equivalent: (1) the market is arbitrage-free; (2) there exists an equivalent martingale measure (risk-neutral probability) $Q$, i.e. a strictly positive probability on $\Omega$ such that $S_j(t)=\mathbb{E}^Q\big[\frac{S_j(t+1)}{1+r(t)}\mid\mathcal{P}_t\big]$ for all $j=1,\dots,N$, $t=0,\dots,T-1$ (equivalently, discounted prices $S_j/B$ are $Q$-martingales). (Theorem 111.)

**[Jan 2024 (1st exam), Q2 (6 pts)]** *Let $Q$ be a RN probability for an arbitrage-free multiperiod market with assets $B,S_1,\dots,S_N$. Then (mark all):* A. $Q(\omega_k)>0$ for all $\omega_k\in\Omega$ — B. $\{S_j(t)\}_t$ is a $Q$-martingale for all $j$ — C. $S_j(t)=\mathbb{E}^Q_t\big[\frac{S_j(t+1)}{1+r(t)}\mid\mathcal{P}_t\big]$ for all $t\le T-1$, all $j$ — D. $\{B(t)\}_t$ is a $Q$-martingale.
**Answer: A, C** (Definition 109). B is false: the **discounted** prices $S_j/B$ are martingales, not $S_j$ (unless $r=0$). D is false: $B$ grows ($B(t+1)=B(t)(1+r(t))>B(t)$ if $r>0$); $B/B=1$ is the trivial martingale.

**[Jan 13, 2025, Q2 (2 pts)]** *$Q$ RN probability of an arbitrage-free multiperiod market. Then:* A. $Q(\omega_k)=0$ for all $\omega_k$ — B. $S_j(t)=\mathbb{E}^Q[\frac{S_j(t+1)}{1+r(t+1)}|\mathcal{P}_t]$ — C. $\{S_j(t)\}$ is a $Q$-martingale — D. $S_j(t)=\mathbb{E}^Q[\frac{S_j(t+1)}{1+r(t)}|\mathcal{P}_t]$.
**Answer: D.** A: must be $>0$. B: wrong rate — the rate over $[t,t+1]$ is $r(t)$ (known at $t$), not $r(t+1)$. C: only discounted prices are martingales.

