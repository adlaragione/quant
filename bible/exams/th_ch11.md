#### [Jan 14, 2022 General — Q2] · [Jan 14, 2022 2nd Partial — Q2] (6 points, mark all the appropriate answers)
**Question.** Let $Q$ denote any risk-neutral probability for an arbitrage-free discrete multiperiod market. Consider the redundant cashflow $X=\{X(t)\}_{t=1}^T$ and let $S_X=\{S_X(t)\}_{t=0}^T$ be its price process. The extended market is arbitrage free if and only if…

- **A.** $S_X(t)=V_{\vartheta^X}(t)$ for all $t=0,\dots,T$ and for every replicating strategy $\vartheta^X$
- **B.** $S_X(t)=\sum_{\tau=t+1}^T\mathbb{E}^Q\Big[\frac{B(t)}{B(\tau)}X(\tau)\,\Big|\,\mathcal{P}_t\Big]$ for all $t=0,\dots,T-1$
- **C.** $\begin{cases}S_X(t)=\mathbb{E}^Q\Big[\frac{X(t+1)}{1+r(t)}\Big|\mathcal{P}_t\Big] & t=0,\dots,T-2\\[4pt] S_X(T-1)=\mathbb{E}^Q\Big[\frac{X(T)}{1+r(T-1)}\Big|\mathcal{P}_{T-1}\Big] & t=T-1\end{cases}$
- **D.** $\begin{cases}S_X(t)=\mathbb{E}^Q\Big[\frac{X(t+1)+S_X(t+1)}{1+r(t)}\Big|\mathcal{P}_t\Big] & t=0,\dots,T-2\\[4pt] S_X(T-1)=\mathbb{E}^Q\Big[\frac{X(T)}{1+r(T-1)}\Big|\mathcal{P}_{T-1}\Big] & t=T-1\end{cases}$

**Correct answers: A, B, D.**
- A = replication (Prop. 123, item 2); D = risk-neutral recursion (Prop. 123, item 3); B = Gordon's formula, equivalent to D.
- C is wrong: it forgets the next-period ex-dividend price $S_X(t+1)$.

#### [Jan 16, 2023 General — Q4] · [Jan 16, 2023 2nd Partial — Q4] (4 points, mark the appropriate alternatives)
**Question.** Let $Q$ denote any risk-neutral probability for an arbitrage-free discrete multiperiod market. Consider the redundant cashflow $X=\{X(t)\}_{t=1}^T$ and let $S_X=\{S_X(t)\}_{t=0}^T$ be its price process. The extended market is arbitrage free if…

- **A.** $S_X(t)=C_{\vartheta^X}(t)$ for $t=0,\dots,T$ and for every replicating strategy $\vartheta^X$
- **B.** $\begin{cases}S_X(t)=\mathbb{E}^Q\Big[\frac{X(t+1)+S_X(t+1)}{1+r(t)}\Big|\mathcal{P}_t\Big] & t=0,\dots,T-2\\[4pt] S_X(T-1)=\mathbb{E}^Q\Big[\frac{X(T)}{1+r(T-1)}\Big|\mathcal{P}_{T-1}\Big] & t=T-1\end{cases}$ and for any $Q$
- **C.** $S_X(t)=\sum_{\tau=t+1}^T\mathbb{E}^Q\Big[\frac{X(\tau)}{B(\tau)}\Big|\mathcal{P}_t\Big]$ for $t=0,\dots,T-1$ and for any $Q$
- **D.** $S_X(t)=\mathbb{E}^Q\Big[\frac{X(t+1)}{1+r(t)}\Big|\mathcal{P}_t\Big]$ for $t=0,\dots,T-1$ and for any $Q$

**Correct answer: B.**
- A is wrong: the price equals the *value* $V_{\vartheta^X}(t)$, not the cashflow $C_{\vartheta^X}(t)$.
- C misses the factor $B(t)$ (it gives $S_X(t)/B(t)$, not $S_X(t)$).
- D forgets $S_X(t+1)$.

#### [Feb 1, 2023 General — Q4] · [Feb 1, 2023 2nd Partial — Q4] (6 points)
**Question.** Let $Q$ denote any risk-neutral probability for an arbitrage-free discrete multiperiod market. Consider the redundant **European** derivative with maturity $T$, cashflow $X=\{X(t)\}_{t=1}^T$, and let $S_X=\{S_X(t)\}_{t=0}^T$ be its price process. In order for the extended market to be arbitrage free we must have…

- **A.** $S_X(t)=C_{\vartheta^X}(t)$ for all $t=0,\dots,T-1$ and for every replicating strategy $\vartheta^X$
- **B.** $S_X(t)=X(t)$ for all $t=0,\dots,T-1$
- **C.** $S_X(t)=\mathbb{E}^Q\Big[\frac{B(t)}{B(T)}X(T)\Big|\mathcal{P}_t\Big]$ for all $t=0,\dots,T-1$
- **D.** $S_X(t)=\mathbb{E}^Q\Big[\frac{S_X(t+1)}{1+r(t)}\Big|\mathcal{P}_t\Big]$ for $t=0,1,\dots,T-1$

**Correct answers: C, D.** For a European claim $X(t)=0$ for $t<T$ and $S_X(T)=X(T)$, so Prop. 123's recursion becomes D and Gordon's formula becomes C. A confuses value and cashflow ($C_{\vartheta^X}(t)=0$ for $t<T$); B is meaningless.
