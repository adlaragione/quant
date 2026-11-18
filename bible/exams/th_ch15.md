#### [Jan 14, 2022 General — Q4] · [Jan 14, 2022 2nd Partial — Q4] (4 points, mark the only appropriate alternative)
**Question.** Let $N(a,b^2)$ denote a normal random variable with mean $a$ and variance $b^2$. In the Black–Scholes model and with respect to the historical measure $P$ the log-price of the risky security $S$ is

- **A.** $\ln\frac{S(t)}{S(0)}\overset{P}{\sim}N(\mu t,\ \sigma^2t)$
- **B.** $\ln\frac{S(t)}{S(0)}\overset{P}{\sim}N\big((\mu-\tfrac{\sigma^2}{2})t,\ \sigma^2t\big)$
- **C.** $\ln\frac{S(t)}{S(0)}\overset{P}{\sim}N\big((\mu-\tfrac{\sigma^2}{2})t,\ \sigma t\big)$
- **D.** $\ln\frac{S(t)}{S(0)}\overset{P}{\sim}N\big((\mu+\tfrac{\sigma^2}{2})t,\ \sigma^2t\big)$

**Correct answer: B** (from Prop. 158: $\ln\frac{S(t)}{S_0}=(\mu-\frac12\sigma^2)t+\sigma W^P(t)$, $W^P(t)\sim N(0,t)$). C has the wrong variance ($\sigma t$ instead of $\sigma^2 t$).

#### [Jan 31, 2022 General — Question 4] (4 points, mark the only appropriate alternative)
**Question.** Let $N(a,b^2)$ denote a normal random variable with mean $a$ and variance $b^2$. In the Black–Scholes model and with respect to the risk-neutral measure $Q$ the log-price of the risky security $S$ is

- **A.** $\ln\frac{S(t)}{S(0)}\overset{Q}{\sim}N(rt,\ \sigma^2t)$
- **B.** $\ln\frac{S(t)}{S(0)}\overset{Q}{\sim}N\big((\mu-\tfrac{\sigma^2}{2})t,\ \sigma^2t\big)$
- **C.** $\ln\frac{S(t)}{S(0)}\overset{Q}{\sim}N\big((r-\tfrac{\sigma^2}{2})t,\ \sigma^2t\big)$
- **D.** $\ln\frac{S(t)}{S(0)}\overset{Q}{\sim}N\big((r+\tfrac{\sigma^2}{2})t,\ \sigma^2t\big)$

(The exam writes the risk-free rate as $\delta$.) **Correct answer: C** (Prop. 165: under $Q$ the drift $\mu$ is replaced by $r$).

#### [Jan 2024 1st exam — Question 4] (4 points, mark the only appropriate alternative)
**Question.** Consider the risky security $S$ in the Black–Scholes model. Let $W$ denote the standard Brownian motion with respect to the historical probability $P$. Then, with respect to $P$, the log-price of $S$ satisfies

- **A.** $d\ln S(t)=\mu\,dt+\sigma\,dW(t)$
- **B.** $d\ln S(t)=\big(\mu-\frac{\sigma^2}2\big)dt+\sigma^2\,dW(t)$
- **C.** $d\ln S(t)=\big(\mu-\frac{\sigma^2}2\big)dt+\sigma\,dW(t)$
- **D.** $d\ln S(t)=\big(\mu-\frac{\sigma^2}2\big)t+\sigma\,W(dt)$

**Correct answer: C** (Itô on $\ln S$, step 3 of the proof of Prop. 158). B has $\sigma^2$ in front of $dW$; D is meaningless notation.

#### [Jan 2024 2nd exam — Question 4] (4 points, mark the only appropriate alternative)
**Question.** Consider the risky security $S$ in the Black–Scholes model. Let $W$ denote the standard Brownian motion with respect to $P$. Then, with respect to $P$, the expected value of $S(t)$ is

- **A.** $\mathbb{E}^P[S(t)]=S_0\,e^{(\mu-\frac{\sigma^2}2)t+\sigma W(t)}$
- **B.** $\mathbb{E}^P[S(t)]=S_0\,e^{(\mu-\frac{\sigma^2}2)t}$
- **C.** $\mathbb{E}^P[S(t)]=S_0\,e^{\mu t}$
- **D.** $\mathbb{E}^P[S(t)]=S(t)$

**Correct answer: C** (Lemma 159). A is $S(t)$ itself (random); B is the median of $S(t)$.

#### [Jan 13, 2025 — Question 4] (6 points, mark all appropriate alternatives)
**Question.** Consider the risky security $S$ in the Black–Scholes model. Let $W$ denote the standard Brownian motion with respect to $P$. Then, with respect to $P$, the risky security $S$ satisfies

- **A.** $dS(t)=\mu\,dt+\sigma\,dW(t)$
- **B.** $d\ln S(t)=\big(\mu-\frac{\sigma^2}2\big)dt+\sigma^2\,dW(t)$
- **C.** $dS(t)=\mu S(t)\,dt+\sigma S(t)\,dW(t)$
- **D.** $d\ln S(t)=\big(\mu-\frac{\sigma^2}2\big)dt+\sigma\,dW(t)$

**Correct answers: C, D.** A is an arithmetic BM (missing the factor $S$); B has $\sigma^2$ instead of $\sigma$ in front of $dW$.

#### [Dec 19, 2025 — Question 4] (4 points, mark all appropriate answers)
**Question.** Consider the risky security $S$ in the Black–Scholes model. Let $W$ denote the standard Brownian motion with respect to $P$. Then, with respect to $P$, the risky security $S$ satisfies

- **A.** $\frac{dS(t)}{S(t)}=\mu\,dt+\sigma\,dW(t)$
- **B.** $d\ln S(t)=\mu\,dt+\sigma\,dW(t)$
- **C.** $dS(t)=\big(\mu-\frac{\sigma^2}2\big)S(t)\,dt+\sigma S(t)\,dW(t)$
- **D.** $d\ln S(t)=\big(\mu-\frac{\sigma^2}2\big)dt+\sigma\,dW(t)$

**Correct answers: A, D.** B forgets the Itô correction; C puts the correction in the wrong equation.
