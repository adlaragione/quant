**[Jan 14, 2022 – General, Q4 (4 pts)]** *Let $N(a,b^2)$ be normal with mean $a$, variance $b^2$. In the BS model, under $P$, the log-price $\ln\frac{S(t)}{S(0)}$ is distributed as (only one):*
- A. $N(\mu t,\sigma^2t)$ — B. $N\big((\mu-\frac{\sigma^2}{2})t,\sigma^2t\big)$ — C. $N\big((r-\frac{\sigma^2}{2})t,\sigma^2t\big)$ — D. $N\big((\mu+\frac{\sigma^2}{2})t,\sigma^2t\big)$

**Answer: B.** From Prop. 158: $\ln\frac{S(t)}{S_0}=(\mu-\frac12\sigma^2)t+\sigma W^P(t)$, $W^P(t)\sim N(0,t)$. (C would be the distribution under $Q$.)

**[Jan 31, 2022 – General, Q4 (4 pts)]** *In the BS model, under the risk-neutral measure $Q$, $\ln\frac{S(t)}{S(0)}$ is distributed as (only one):* A. $N(rt,\sigma^2t)$ — B. $N((\mu-\frac{\sigma^2}2)t,\sigma^2t)$ — C. $N((r-\frac{\sigma^2}2)t,\sigma^2t)$ — D. $N((r+\frac{\sigma^2}{2})t,\sigma^2t)$.
**Answer: C** (Prop. 165: under $Q$ the drift $\mu$ is replaced by $r$).

**[Jan 2024 (1st exam), Q4 (4 pts)]** *Under $P$, the log-price of $S$ in the BS model satisfies (only one):* A. $d\ln S=\mu dt+\sigma dW$ — B. $d\ln S=(\mu-\frac{\sigma^2}2)dt+\sigma dW$ — C. $d\ln S=(\mu+\frac{\sigma^2}{2})dt+\sigma dW$ — D. $d\ln S=(\mu-\frac{\sigma^2}2)t+\sigma W(dt)$.
**Answer: B** (Itô on $\ln S$, step 3 of the proof of Prop. 158).

**[Jan 2024 (2nd exam), Q4 (4 pts)]** *Under $P$ in the BS model, $\mathbb{E}^P[S(t)]=$ (only one):* A. $S_0e^{(\mu-\frac{\sigma^2}2)t+\sigma W(t)}$ — B. $S_0e^{(\mu-\frac{\sigma^2}2)t}$ — C. $S_0e^{\mu t}$ — D. $S(t)$.
**Answer: C** (Lemma 159). A is $S(t)$ itself (random); B is the median.

**[Jan 13, 2025, Q4 (6 pts)]** *Under $P$, the risky security satisfies (mark all):* A. $dS=\mu dt+\sigma dW$ — B. $d\ln S=(\mu-\frac{\sigma^2}{2})dt+\sigma dW$ — C. $dS=\mu S\,dt+\sigma S\,dW$ — D. $d\ln S=(\mu+\frac{\sigma^2}{2})dt+\sigma dW$.
**Answer: B, C.** A is an arithmetic BM (missing the factor $S$); D has the wrong sign of the Itô correction.

**[Dec 19, 2025, Q4 (4 pts)]** *Under $P$ (mark all):* A. $\frac{dS}{S}=\mu dt+\sigma dW$ — B. $d\ln S=\mu dt+\sigma dW$ — C. $dS=(\mu-\frac{\sigma^2}{2})S\,dt+\sigma S\,dW$ — D. $d\ln S=(\mu-\frac{\sigma^2}{2})dt+\sigma dW$.
**Answer: A, D.**

