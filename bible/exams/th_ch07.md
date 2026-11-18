#### [Jan 16, 2023 General — Question 3] (6 points, mark the appropriate alternatives)
**Question.** Consider a (non-constant) $\mathcal{P}_t$-measurable random variable $X$. Then…

- **A.** the $\mathcal{P}_t$-conditional expectation of $X$ is equal to the unconditional expectation of $X$
- **B.** the $\mathcal{P}_t$-conditional expectation of $X$ is equal to $X$ itself
- **C.** $X$ takes all its possible realizations on all $f^t_h\in\mathcal{P}_t$
- **D.** $X$ is constant on each $f^t_h\in\mathcal{P}_t$

**Correct answers: B, D.**
- D is Definition 77; B is Remark 80 ($\mathbb{E}[X|\mathcal{P}_t]=X$ for measurable $X$).
- A would hold for $X$ *independent* of $\mathcal{P}_t$ (Prop. 86), not for a non-constant measurable $X$.
- C is the opposite of measurability.

#### [Feb 1, 2023 General — Question 3] (4 points, mark the appropriate alternatives)
**Question.** Consider a random variable $X:\Omega\to\{x_1,\dots,x_M\}$ independent of $\mathcal{P}_t$ for some $t\in\{1,\dots,T\}$ with respect to the probability measure $Q$. Denote $\{X=x_m\}=\{\omega\in\Omega:X(\omega)=x_m\}$ and assume $Q[\{X=x_m\}]>0$ for all $m=1,\dots,M$. Then

- **A.** $\mathbb{E}^Q[X|\mathcal{P}_t]=\mathbb{E}^Q[X]$
- **B.** $\mathbb{E}^Q[X|\mathcal{P}_t]=X$
- **C.** $\{X=x_m\}\cap f^t_h\neq\emptyset$ for all $m=1,\dots,M$ and for all $f^t_h\in\mathcal{P}_t$
- **D.** $Q[\{X=x_m\}\cap f^t_h]=1$ for all $m=1,\dots,M$ and for all $f^t_h\in\mathcal{P}_t$

**Correct answers: A, C.**
- A is Proposition 86.
- C: by independence $Q[\{X=x_m\}\cap f^t_h]=Q[X=x_m]\,Q[f^t_h]>0$, so the intersection cannot be empty: every value of $X$ is still possible in every cell.
- B would require measurability; D is impossible (disjoint events cannot all have probability 1).
