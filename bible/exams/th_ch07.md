**[Jan 16, 2023 – General, Q3 (6 pts)]** *Consider a (non-constant) $\mathcal{P}_t$-measurable r.v. $X$. Then… (mark all)*
A. its $\mathcal{P}_t$-conditional expectation equals its unconditional expectation — B. its $\mathcal{P}_t$-conditional expectation equals $X$ itself — C. $X$ takes all its possible realizations on all $f^t_h\in\mathcal{P}_t$ — D. $X$ is constant on each $f^t_h\in\mathcal{P}_t$.
**Answer: B, D.** D is Definition 77; B is Remark 80. A would hold for $X$ independent of $\mathcal{P}_t$ (Prop. 86), not measurable (and non-constant). C is the opposite of measurability.

**[Feb 1, 2023, Q3 (4 pts)]** *$X:\Omega\to\{x_1,\dots,x_M\}$ independent of $\mathcal{P}_t$ under $Q$, with $Q[\{X=x_m\}]>0$ for all $m$. Then:* A. $\mathbb{E}^Q[X|\mathcal{P}_t]=\mathbb{E}^Q[X]$ — B. $\mathbb{E}^Q[X|\mathcal{P}_t]=X$ — C. $\{X=x_m\}\cap f^t_h\neq\emptyset$ for all $m$ and all $f^t_h\in\mathcal{P}_t$ — D. $Q[\{X=x_m\}\cap f^t_h]=1$ for all $m,h$.
**Answer: A, C.** A is Prop. 86. C: by independence $Q[\{X=x_m\}\cap f^t_h]=Q[X=x_m]\,Q[f^t_h]>0$ (both factors positive), so the intersection cannot be empty — every value of $X$ is still possible in every cell. B would require measurability; D is absurd (probabilities of disjoint events cannot all be 1).

