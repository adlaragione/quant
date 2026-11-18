**[Jan 14, 2022 – General, Q3 (4 pts); same in Jan 14, 2022 2nd partial]** *Let $dX=a(t,X)dt+b(t,X)dW$, $X(0)=X_0$, $\varphi\in C^{1,2}$, $Y(t)=\varphi(t,X(t))$. Then $Y$ satisfies (only one answer):*
- A. $dY=[\varphi_t+\varphi_xa+\varphi_{xx}b^2]dt+\varphi_xb\,dW$
- B. $dY=[\varphi_t+\varphi_xa+\tfrac12\varphi_{xx}b^2]dt+\varphi_xb\,dW$
- C. (a variant with a wrong sign / wrong placement of a term)
- D. $dY=[\varphi_t+\varphi_x+\tfrac12\varphi_{xx}]dt+\varphi_x\,dW$

**Answer: B** (Itô's formula, Lemma 150: factor $\tfrac12$ on $\varphi_{xx}b^2$; $\varphi_x$ multiplies $a$ in the drift and $b$ in the diffusion term). A misses the $\frac12$; D forgets the coefficients $a,b$.

**[Jan 16, 2023 – 2nd Partial, Q3 (6 pts)]** *Let $dX=a(t,X)dt+b(t,X)dW$, $X(0)=X_0$; $\varphi\in C^{1,2}$. Applying Itô's lemma, write the stochastic differential of $\varphi(t,X(t))$.*
**Answer.** $d\varphi(t,X(t))=\Big[\frac{\partial\varphi}{\partial t}+\frac{\partial\varphi}{\partial x}a(t,X(t))+\frac12\frac{\partial^2\varphi}{\partial x^2}b^2(t,X(t))\Big]dt+\frac{\partial\varphi}{\partial x}b(t,X(t))\,dW(t)$, all derivatives evaluated at $(t,X(t))$. (Lemma 150 with $\alpha=a(t,X(t))$, $\beta=b(t,X(t))$.)

*(Q2 and Q4 of this exam are identical to Q2 and Q4 of the Jan 16, 2023 General exam.)*

