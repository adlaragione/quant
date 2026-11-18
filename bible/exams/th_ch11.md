**[Jan 14, 2022 – General, Q2 (6 pts) — also Jan 14, 2022 2nd partial Q2]** *Let $Q$ be any RN probability for an arbitrage-free discrete multiperiod market. Consider the redundant cashflow $X=\{X(t)\}_{t=1}^T$ with price process $S_X=\{S_X(t)\}_{t=0}^T$. The extended market is arbitrage-free iff… (mark all appropriate answers)*
- A. $S_X(t)=V_{\vartheta_X}(t)$ for all $t=0,\dots,T$ and every replicating strategy $\vartheta_X$
- B. $S_X(t)=\sum_{\tau=t+1}^T\mathbb{E}^Q\big[\frac{B(t)}{B(\tau)}X(\tau)\mid\mathcal{P}_t\big]$ for all $t=0,\dots,T-1$
- C. $S_X(t)=\mathbb{E}^Q\big[\frac{X(t+1)}{1+r(t)}\mid\mathcal{P}_t\big]$ for $t\le T-2$ and $S_X(T-1)=\mathbb{E}^Q\big[\frac{X(T)}{1+r(T-1)}\mid\mathcal{P}_{T-1}\big]$
- D. $S_X(t)=\mathbb{E}^Q\big[\frac{X(t+1)+S_X(t+1)}{1+r(t)}\mid\mathcal{P}_t\big]$ for $t\le T-2$ and $S_X(T-1)=\mathbb{E}^Q\big[\frac{X(T)}{1+r(T-1)}\mid\mathcal{P}_{T-1}\big]$

**Answer: A, B, D.** A = replication (Prop. 123 item 2); D = risk-neutral recursion (Prop. 123 item 3); B = Gordon's formula, equivalent to D. C is wrong: it forgets the next-period ex-dividend price $S_X(t+1)$ (it would be right only if $X$ paid at a single date $t+1$).

**[Jan 16, 2023 – General, Q4 (4 pts)]** *$Q$ any RN probability of an arbitrage-free multiperiod market; redundant cashflow $X$, price process $S_X$. The extended market is arbitrage-free if… (mark all)*
A. $S_X(t)=C_{\vartheta_X}(t)$ for all $t$ and every replicating $\vartheta_X$ — B. $S_X(t)=\mathbb{E}^Q[\frac{X(t+1)+S_X(t+1)}{1+r(t)}|\mathcal{P}_t]$, $t\le T-2$, $S_X(T-1)=\mathbb{E}^Q[\frac{X(T)}{1+r(T-1)}|\mathcal{P}_{T-1}]$, for any $Q$ — C. $S_X(t)=\sum_{\tau=t+1}^T\mathbb{E}^Q[\frac{X(\tau)}{B(\tau)}|\mathcal{P}_t]$ for any $Q$ — D. $S_X(t)=\mathbb{E}^Q[\frac{X(t+1)}{1+r(t)}|\mathcal{P}_t]$ for any $Q$.
**Answer: B.** A is wrong: the price equals the **value** $V_{\vartheta_X}(t)$, not the cashflow $C_{\vartheta_X}(t)$. C misses the factor $B(t)$ (it would give $S_X(t)/B(t)$). D forgets $S_X(t+1)$.

**[Feb 1, 2023, Q4 (6 pts)]** *Redundant **European** derivative with maturity $T$ (cashflow only at $T$), price process $S_X$. For NA we must have…* A. $S_X(t)=C_{\vartheta_X}(t)$, $t\le T-1$ — B. $S_X(t)=X(t)$, $t\le T-1$ — C. $S_X(t)=\mathbb{E}^Q\big[\frac{B(t)}{B(T)}X(T)\mid\mathcal{P}_t\big]$, $t\le T-1$ — D. $S_X(t)=\mathbb{E}^Q\big[\frac{S_X(t+1)}{1+r(t)}\mid\mathcal{P}_t\big]$, $t=0,\dots,T-1$.
**Answer: C, D.** For a European claim $X(t)=0$ for $t<T$ and $S_X(T)=X(T)$, so Prop. 123's recursion becomes D and Gordon's formula becomes C. A confuses value and cashflow ($C_{\vartheta_X}(t)=0$ for $t<T$); B is meaningless.

