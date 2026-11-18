#### [Jan 14, 2022 General — Q3] · [Jan 14, 2022 2nd Partial — Q3] (4 points, mark the only appropriate alternative)
**Question.** Consider a diffusion process $\{X(t)\}_{t\in[0,T]}$ satisfying the SDE $dX(t)=a(t,X(t))\,dt+b(t,X(t))\,dW(t)$ with $X(0)=X_0$. Assume $\varphi:[0,T]\times\mathbb{R}\to\mathbb{R}$ continuously differentiable, once with respect to the first variable $t$, twice with respect to the second $x$. Let $Y(t)=\varphi(t,X(t))$. Then the process $Y$ satisfies

- **A.** $dY=\Big[\frac{\partial\varphi}{\partial t}+\frac{\partial\varphi}{\partial x}a+\frac{\partial^2\varphi}{\partial x^2}b^2\Big]dt+\frac{\partial\varphi}{\partial x}b\,dW$
- **B.** $dY=\Big[\frac{\partial\varphi}{\partial t}+\frac{\partial\varphi}{\partial x}a+\frac12\frac{\partial^2\varphi}{\partial x^2}b^2\Big]dt+\frac{\partial\varphi}{\partial x}b\,dW$
- **C.** $dY=\Big[\Big(\frac{\partial\varphi}{\partial t}+\frac{\partial\varphi}{\partial x}\Big)a+\frac12\frac{\partial^2\varphi}{\partial x^2}b^2\Big]dt+\frac{\partial\varphi}{\partial x}b\,dW$
- **D.** $dY=\Big[\frac{\partial\varphi}{\partial t}+\frac{\partial\varphi}{\partial x}+\frac12\frac{\partial^2\varphi}{\partial x^2}\Big]dt+\frac{\partial\varphi}{\partial x}dW$

(all derivatives evaluated at $(t,X(t))$; $a,b$ at $(t,X(t))$)

**Correct answer: B** (Itô's formula, Lemma 150).
- A misses the factor $\frac12$.
- C wrongly multiplies $\varphi_t$ by $a$.
- D forgets the coefficients $a$ and $b$.

#### [Jan 16, 2023 2nd Partial — Question 3] (6 points, open question)
**Question.** Consider a diffusion process $\{X(t)\}_{t\in[0,T]}$ satisfying $dX(t)=a(t,X(t))\,dt+b(t,X(t))\,dW(t)$ with $X(0)=X_0$. Assume $\varphi:[0,T]\times\mathbb{R}\to\mathbb{R}$ to be a function of $t$ and $x$, continuously differentiable w.r.t. $t$ and twice continuously differentiable w.r.t. $x$. Applying Itô's lemma, write the stochastic differential of $\varphi(t,X(t))$.

**Answer.**
$$d\varphi(t,X(t))=\Big[\frac{\partial\varphi}{\partial t}+\frac{\partial\varphi}{\partial x}a(t,X(t))+\frac12\frac{\partial^2\varphi}{\partial x^2}b^2(t,X(t))\Big]dt+\frac{\partial\varphi}{\partial x}b(t,X(t))\,dW(t),$$
all derivatives evaluated at $(t,X(t))$.
