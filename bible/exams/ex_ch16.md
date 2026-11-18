*All Black–Scholes exercises share the same text structure:* "Consider a Black–Scholes market with the riskless security $B(t)=e^{rt}$ and the lognormal risky security $S$ with drift $\mu$ and volatility $\sigma$ under the historical probability $P$. Express your results in terms of the distribution function $N(\cdot)$ of a standard normal random variable whenever appropriate." (The exams write the riskless rate as $\delta$.) Each exercise below gives its parameters.

### [Jan 14, 2022 — General and 2nd Partial] Exercise 2 (35 points)

**Text.** $S(0)=10$, $r=3\%$, $\mu=7\%$, $\sigma=20\%$, $T=2$. Let $R(t)=\ln\frac{S(t)}{S(0)}$ be the continuously compounded return; recall $R(t)=(\mu-\frac{\sigma^2}2)t+\sigma W^P(t)=(r-\frac{\sigma^2}2)t+\sigma W^Q(t)$.

**1.** *(5 points)* Compute the historical probability that this return is greater than $rT$ at $T=2$, i.e. $P[R(T)>rT]$. Is it larger or smaller than 50%?

> **Solution.** $R(T)=(\mu-\frac{\sigma^2}{2})T+\sigma\sqrt TZ$ ⇒ $P\big[Z>\frac{(r-\mu+\frac{\sigma^2}2)\sqrt T}{\sigma}\big]=1-N(-0.1414)=N(0.1414)\approx0.556$ — **larger than 50%**.

**2.** *(5 points)* A forward contract on $R$ is introduced, with payoff $X(2)=R(2)-F$ at $T=2$; $F$ is set at $t=0$ so that the NA price of the forward at $t=0$ is zero. Determine $F$.

> **Solution.** $0=e^{-rT}\mathbb{E}^Q[R(T)-F]$ ⇒ $F=\mathbb{E}^Q[R(T)]=(r-\frac{\sigma^2}2)T=(0.03-0.02)\cdot2=$ **0.02**.

**3.** *(5 points)* Compute $P[X(2)>0]$. Is it increasing or decreasing with respect to $\sigma$? Justify.

> **Solution.** $P[R(T)>F]=P\big[Z>\frac{F-(\mu-\frac{\sigma^2}2)T}{\sigma\sqrt T}\big]=P\big[Z>\frac{(r-\mu)T}{\sigma\sqrt T}\big]=N\big(\frac{(\mu-r)\sqrt T}{\sigma}\big)=N(0.2828)\approx0.611$. Since $\mu-r>0$ and $\sigma$ appears only in the denominator, it is **decreasing in $\sigma$**.

**4.** *(4 points)* Find $S_X(t)$, the NA price of the forward at any $t\in[0,T]$.

> **Solution.** $S_X(t)=e^{-r(T-t)}\mathbb{E}^Q_t[R(T)-F]$ with $\mathbb{E}^Q_t[R(T)]=(r-\frac{\sigma^2}2)T+\sigma W^Q(t)$ ⇒ $S_X(t)=e^{-r(T-t)}\sigma W^Q(t)$, i.e.
> $$S_X(t)=e^{-r(T-t)}\Big[\ln\tfrac{S(t)}{S(0)}-\big(r-\tfrac{\sigma^2}{2}\big)t\Big].$$

**5.** *(3 points)* Find the replicating portfolio $\vartheta(t)=(\vartheta_0(t),\vartheta_1(t))$ ($\vartheta_0$ units of $B$, $\vartheta_1$ units of $S$).

> **Solution.** $\vartheta_1(t)=\frac{\partial S_X}{\partial S}=\frac{e^{-r(T-t)}}{S(t)}$; $\vartheta_0(t)=e^{-rt}[S_X(t)-\vartheta_1S(t)]=e^{-rT}\big[\ln\frac{S(t)}{S(0)}-(r-\frac{\sigma^2}2)t-1\big]$.

**6.** *(3 points)* Is the replicating portfolio long or short on $S$?

> **Solution.** $\vartheta_1>0$ ⇒ **long**.

**7.** *(5 points)* Compute the historical mean and variance of $\Delta R=R(2)-R(1)$.

> **Solution.** $\Delta R=(\mu-\frac{\sigma^2}2)+\sigma(W^P(2)-W^P(1))\sim N(\mu-\frac{\sigma^2}{2},\sigma^2)$: mean **0.05**, variance **0.04**.

**8.** *(5 points)* Express $X(2)$ in terms of $\Delta R$ and $R(1)$ and compute $P[X(2)>0\mid\mathcal{F}_1]$. Determine the values of $S(1)$ such that $P[X(2)>0\mid\mathcal{F}_1]\ge0.5$.

> **Solution.** $X(2)=\Delta R+R(1)-F$ with $R(1)=x$ $\mathcal{F}_1$-measurable and $\Delta R$ independent of $\mathcal{F}_1$: $P_1[\Delta R>F-x]=N\big(\frac{x-F+\mu-\frac{\sigma^2}2}{\sigma}\big)\ge0.5$ ⇔ $x\ge F-(\mu-\frac{\sigma^2}2)=-0.03$ ⇔ $S(1)\ge10e^{-0.03}\approx$ **9.70**.

### [Jan 31, 2022 — General] Exercise 2 (35 points)

**Text.** $S(0)=1$, $r=2\%$, $\mu=5\%$, $\sigma=15\%$, $T=2$.

**1.** *(6 points)* Compute the historical probability that a European call on $S$ with maturity $T=2$ and strike $K=0.8$ closes in the money.

> **Solution.** $P[S(2)>0.8]=N\Big(\frac{\ln(S_0/K)+(\mu-\frac{\sigma^2}2)T}{\sigma\sqrt T}\Big)=N\Big(\frac{0.2231+0.0775}{0.2121}\Big)=N(1.4172)\approx0.922$.

**2.** *(6 points)* Write the NA price of the call of Point 1 for all $t\in[0,T]$.

> **Solution.** $c(t)=S(t)N(d_1)-0.8e^{-0.02(2-t)}N(d_2)$, $d_1=\frac{\ln\frac{S(t)}{0.8}+0.03125(2-t)}{0.15\sqrt{2-t}}$, $d_2=d_1-0.15\sqrt{2-t}$.

**3.** *(5 points)* Consider a call with $T=2$ and strike $K=S(0)$; compute the RN probability that it closes in the money as a function of $\sigma$. Find the values of $\sigma$ for which this probability is $\ge50\%$.

> **Solution.** $Q[S(T)>S_0]=N\big(\frac{(r-\frac{\sigma^2}2)\sqrt T}{\sigma}\big)\ge\frac12$ ⇔ $r-\frac{\sigma^2}{2}\ge0$ ⇔ **$0<\sigma\le\sqrt{2r}=20\%$**.

**4.** *(6 points)* Assume $\sigma=15\%$ from now on. Compute the RN mean and variance of $\ln\big(S(\tfrac T2)S(T)\big)$.

> **Solution.** $Y=2\ln S_0+(r-\frac{\sigma^2}2)\frac{3T}{2}+\sigma\big[2W^Q(\tfrac T2)+(W^Q(T)-W^Q(\tfrac T2))\big]$; the increments are independent $N(0,\frac T2)$ ⇒ $Y\sim N\big(0.02625,\ 5\sigma^2\tfrac T2=0.1125\big)$.

**5.** *(5 points)* Consider the European derivative with payoff $X(T)=\sqrt{S(\tfrac T2)S(T)}$ at $T=2$. Compute its NA price at $t=0$.

> **Solution.** $X=e^{Y/2}$ and $\mathbb{E}[e^{N(a,b^2)}]=e^{a+b^2/2}$ ⇒ $S_X(0)=e^{-0.04}\exp\big(\frac{0.02625}{2}+\frac{0.1125}{8}\big)=e^{-0.0128125}\approx$ **0.98727**.

**6.** *(4 points)* Find $S_X(t)$ for $t\in[\tfrac T2,T]$.

> **Solution.** $S(\frac T2)$ is known ⇒ $S_X(t)=e^{-r(T-t)}\sqrt{S(\tfrac T2)}\,\mathbb{E}^Q_t[\sqrt{S(T)}]$, with $\mathbb{E}^Q_t[\sqrt{S(T)}]=\sqrt{S(t)}\,e^{\frac12(r-\frac{\sigma^2}2)(T-t)+\frac{\sigma^2}8(T-t)}$ ⇒
> $$S_X(t)=\sqrt{S(\tfrac T2)S(t)}\;e^{-(\frac r2+\frac{\sigma^2}{8})(T-t)}=\sqrt{S(1)S(t)}\;e^{0.0128125\,t-0.025625}.$$

**7.** *(3 points)* Find $S_X(t)$ for $t\in[0,\tfrac T2]$.

> **Solution.** $\sqrt{S(\frac T2)S(T)}=S(t)\exp\big[(r-\frac{\sigma^2}{2})(\frac{3T}4-t)+\frac\sigma2\big(2(W^Q_{T/2}-W^Q_t)+(W^Q_T-W^Q_{T/2})\big)\big]$; the Gaussian part has variance $\frac{\sigma^2}{4}(\frac{5T}{2}-4t)$; after multiplying by $e^{-r(T-t)}$ all $t$-terms cancel:
> $$S_X(t)=S(t)\exp\Big(-\frac{rT}{4}-\frac{\sigma^2T}{16}\Big)=0.98727\,S(t).$$

### [Jan 16, 2023 — General and 2nd Partial] Exercise 2 (40 points)

**Text.** $S(0)=1$, $r=4\%$, $\mu=9\%$, $\sigma=25\%$, $T=4$.

**1.** *(5 points)* Compute the historical probability that a European call with strike $K=0.9$ and maturity $T=4$ closes out of the money.

> **Solution.** $P[S(T)<K]=N\Big(\frac{\ln(K/S_0)-(\mu-\frac{\sigma^2}2)T}{\sigma\sqrt T}\Big)=N\Big(\frac{-0.1054-0.235}{0.5}\Big)=N(-0.6807)\approx0.248$.

**2.** *(5 points)* Consider $Y(t)=S^2(t)$. Compute the stochastic differential of $Y$ under $P$ and under $Q$. What is the distribution of $Y$ under $P$ and under $Q$?

> **Solution.** Itô with $f=x^2$ ($f_x=2x$, $f_{xx}=2$): $dY=2S\,dS+\sigma^2S^2dt=Y[(2\mu+\sigma^2)dt+2\sigma dW^P]=Y[(2r+\sigma^2)dt+2\sigma dW^Q]$. $Y$ is **lognormal** under both: drift $2\mu+\sigma^2=0.2425$ under $P$, $2r+\sigma^2=0.1425$ under $Q$; volatility $2\sigma=0.5$.

**3.** *(5 points)* A forward on $Y$ with payoff $X(4)=Y(4)-F$ is introduced; $F$ is set so that its initial NA price is zero. Determine $F$. Is $F$ increasing or decreasing in $\sigma$?

> **Solution.** $F=\mathbb{E}^Q[Y(T)]=S_0^2e^{(2r+\sigma^2)T}=e^{0.57}=$ **1.7683**; **increasing** in $\sigma$.

**4.** *(5 points)* Find $S_X(t)$, the NA value of the forward at any $t\in[0,T]$.

> **Solution.** $S_X(t)=e^{-r(T-t)}(\mathbb{E}^Q_t[Y(T)]-F)=S(t)^2e^{(r+\sigma^2)(T-t)}-Fe^{-r(T-t)}$.

**5.** *(5 points)* Find the replicating portfolio $\vartheta(t)=(\vartheta_0(t),\vartheta_1(t))$.

**6.** *(3 points)* Is it long or short on $S$? And on $B$?

> **Solution (5–6).** $\vartheta_1(t)=2S(t)e^{(r+\sigma^2)(T-t)}>0$ (**long $S$**); $\vartheta_0(t)=e^{-rt}(S_X-\vartheta_1S)=-e^{-rt}\big[S(t)^2e^{(r+\sigma^2)(T-t)}+Fe^{-r(T-t)}\big]<0$ (**short $B$**).

**7.** *(7 points)* Consider the buy-and-hold strategy $\vartheta^{BH}(t)=\vartheta(0)$ for all $t$. Compute the historical mean and variance of its terminal value $V_{\vartheta^{BH}}(T)$. (Hint: $\mathbb{E}[\exp N(a,b^2)]=\exp(a+\frac{b^2}2)$.)

> **Solution.** $\vartheta_0(0)=-e^{(r+\sigma^2)T}-Fe^{-rT}=-3.0137$; $\vartheta_1(0)=2e^{0.41}=3.0136$. $V(T)=\vartheta_0(0)e^{rT}+\vartheta_1(0)S(T)$: $\mathbb{E}^P[V(T)]=-3.0137e^{0.16}+3.0136e^{0.36}=$ **0.7829**; $\operatorname{Var}^P[V(T)]=\vartheta_1(0)^2S_0^2e^{2\mu T}(e^{\sigma^2T}-1)=$ **5.2993**.

**8.** *(5 points)* At $t=1$, find the values of $S(1)$ such that the buy-and-hold strategy super-replicates the forward payoff conditionally in historical expectation: $\mathbb{E}^P_1[V_{\vartheta^{BH}}(4)]>\mathbb{E}^P_1[X(4)]$.

> **Solution.** $\vartheta_0(0)e^{rT}+\vartheta_1(0)xe^{3\mu}>x^2e^{3(2\mu+\sigma^2)}-F$ ⇔ $2.0699x^2-3.9477x+1.7683<0$ ⇔ **$0.7190<S(1)<1.1882$**.

### [Feb 1, 2023 — General and 2nd Partial] Exercise 2 (40 points)

**Text.** $S(0)=1$, $r=3\%$, $\mu=8\%$, $\sigma=20\%$, $T=3$.

**1.** *(5 points)* Compute the historical probability that a European put with strike $K=1.1$ and maturity $T=3$ closes in the money.

> **Solution.** $P[S(3)<1.1]=N\Big(\frac{\ln1.1-(\mu-\frac{\sigma^2}2)3}{\sigma\sqrt3}\Big)=N\Big(\frac{0.0953-0.18}{0.3464}\Big)=N(-0.2445)\approx0.403$.

**2.** *(5 points)* Consider the annual returns $R(1)=\ln\frac{S(1)}{S(0)}$, $R(2)=\ln\frac{S(2)}{S(1)}$, $R(3)=\ln\frac{S(3)}{S(2)}$. Find their risk-neutral distribution.

> **Solution.** $R(t)=(r-\frac{\sigma^2}2)+\sigma(W^Q(t)-W^Q(t-1))\sim N(r-\frac{\sigma^2}{2},\sigma^2)=N(0.01,\ 0.04)$.

**3.** *(5 points)* Are they independent of each other under $Q$? Justify.

> **Solution.** **Yes**: they are functions of non-overlapping Brownian increments, which are independent (Def. 141).

**4.** *(5 points)* Find $Q[R(1)>r]$, $Q[R(2)>r]$, $Q[R(3)>r]$. Are they increasing or decreasing in $\sigma$?

> **Solution.** $Q[R(t)>r]=Q\big[Z>\frac{\sigma}{2}\big]=N(-\frac\sigma2)=N(-0.1)=0.46017=:q$ for all $t$; **decreasing in $\sigma$**.

**5.** *(5 points)* Consider the European derivative that at $T=3$ pays as many coupons $C=10$ as the number of years in which the annual return exceeds the riskless return: $X(3)=C\sum_{t=1}^3I_t$, with $I_t=1$ if $R(t)>r$, $0$ otherwise. Compute $S_X(0)$.

> **Solution.** $S_X(0)=e^{-3r}C\sum_tQ[R(t)>r]=3Ce^{-0.09}N(-0.1)=27.418\,N(-0.1)\approx$ **12.617**.

**6.** *(5 points)* Compute $P[X(3)>25]$.

> **Solution.** $X(3)\in\{0,10,20,30\}$ ⇒ $\{X>25\}=\{\text{all three } I_t=1\}$. Under $P$, $R(t)\sim N(\mu-\frac{\sigma^2}2,\sigma^2)$ i.i.d., $p=P[R(t)>r]=N\big(\frac{\mu-\frac{\sigma^2}{2}-r}{\sigma}\big)=N(0.15)=0.5596$ ⇒ $P[X>25]=N(0.15)^3\approx0.175$.

**7.** *(3 points)* Compute the NA price of the derivative at $t=1$.

> **Solution.** $I_1$ is known ⇒ $S_X(1)=Ce^{-2r}(I_1+2q)=9.4176\,(I_1+2N(-0.1))$.

**8.** *(4 points)* Compute the NA price of the derivative at $t\in(1,2)$.

> **Solution.** $I_1$ known, $I_3$ independent of $\mathcal{F}_t$, and $Q_t[R(2)>r]=N(y_t)$ with $y_t=\frac{\ln\frac{S(t)}{S(1)}+(r-\frac{\sigma^2}{2})(2-t)-r}{\sigma\sqrt{2-t}}$ ⇒ $S_X(t)=Ce^{-r(3-t)}\big[I_1+N(y_t)+N(-0.1)\big]$.

**9.** *(3 points)* At $t\in(1,2)$ find $\vartheta_1(t)$, the number of units of $S$ in the replicating portfolio. Is it long or short on $S$?

> **Solution.** $\vartheta_1(t)=Ce^{-r(3-t)}\frac{\phi(y_t)}{\sigma\sqrt{2-t}\,S(t)}>0$ ⇒ **long**.

### [Jan 2024 — 1st exam] Exercise 2 (40 points)

**Text.** $S(0)=100$, $r=4\%$, $\mu=9\%$, $\sigma=20\%$, $T=2$.

**1.** *(7 points)* Compute the historical probability that a European call with maturity $T=2$ and strike $K=100$ closes in the money. Is it larger or smaller than 50%?

> **Solution.** $P[S(2)>100]=N\big(\frac{(\mu-\frac{\sigma^2}{2})\sqrt T}{\sigma}\big)=N(0.495)\approx0.690$ — **larger**.

**2.** *(6 points)* Consider $R(1)=\ln\frac{S(1)}{S(0)}$ and $R(2)=\ln\frac{S(2)}{S(1)}$. Are they independent under $Q$ and/or under $P$? Are they identically distributed? Justify.

> **Solution.** They are functions of the non-overlapping increments $W(1)-W(0)$ and $W(2)-W(1)$ ⇒ **independent under both $P$ and $Q$**, and **identically distributed** under each measure (stationary increments, same length).

**3.** *(6 points)* Compute the risk-neutral and historical mean and variance of $R(1)$ and $R(2)$.

> **Solution.** Under $Q$: mean $r-\frac{\sigma^2}{2}=0.02$, variance $0.04$. Under $P$: mean $\mu-\frac{\sigma^2}2=0.07$, variance $0.04$.

**4.** *(5 points)* Consider the European derivative with payoff at $T=2$: $X(2)=100\frac{R(1)+R(2)}{2}=50\big(\ln\frac{S(1)}{S(0)}+\ln\frac{S(2)}{S(1)}\big)$. Compute $S_X(0)$.

> **Solution.** $S_X(0)=e^{-2r}\,50\cdot2(r-\frac{\sigma^2}{2})=100e^{-0.08}\cdot0.02\approx$ **1.846**.

**5.** *(7 points)* Compute $P[X(2)>0]$. Is it larger or smaller than 50%?

> **Solution.** $R(1)+R(2)\sim N(0.14,\ 0.08)$ under $P$ ⇒ $P=N\big(\frac{0.14}{\sqrt{0.08}}\big)=N(0.495)>50\%$.

**6.** *(4 points)* Compute the sensitivity of $S_X(0)$ with respect to $\sigma$.

> **Solution.** $S_X(0)=100e^{-rT}(r-\frac{\sigma^2}{2})$ ⇒ $\frac{\partial S_X(0)}{\partial\sigma}=-100\,\sigma\,e^{-rT}<0$.

**7.** *(5 points)* Compute $S_X(t)$ for any $t\in(1,2)$.

> **Solution.** $\mathbb{E}^Q_t\big[\ln\frac{S(2)}{S(0)}\big]=\ln\frac{S(t)}{S(0)}+(r-\frac{\sigma^2}{2})(2-t)$ ⇒ $S_X(t)=50\,e^{-r(2-t)}\big[\ln\frac{S(t)}{S(0)}+(r-\frac{\sigma^2}{2})(2-t)\big]$.

### [Jan 2024 — 2nd exam] Exercise 2 (40 points)

**Text.** $S(0)=1$, $r=5\%$, $\mu=9\%$, $\sigma=30\%$, $T=4$.

**1.** *(5 points)* Compute the historical probability that a European put with maturity $T=4$ and strike $K_p=1.3$ closes in or at the money.

> **Solution.** $P[S(4)\le1.3]=N\Big(\frac{\ln1.3-(\mu-\frac{\sigma^2}{2})4}{0.6}\Big)=N(0.1373)\approx0.555$.

**2.** *(6 points)* Consider the European digital derivative with payoff $X_1(T)=1$ if $S(T)>K$, $0$ otherwise, with $K=1.69$. Find its initial price.

> **Solution.** $S_{X_1}(0)=e^{-rT}N(d_2)=e^{-0.2}N\Big(\frac{\ln\frac{1}{1.69}+(0.05-0.045)4}{0.6}\Big)=0.81873\,N(-0.8412)$.

**3.** *(7 points)* Using Itô's lemma, compute the stochastic differential of $Y(t)=S^2(t)$ under $Q$. What is the RN distribution of $Y$?

> **Solution.** $dY=2S\,dS+\sigma^2S^2dt=Y[(2r+\sigma^2)dt+2\sigma dW^Q]$ ⇒ $Y$ lognormal with RN drift $0.19$ and volatility $0.6$.

**4.** *(8 points)* Consider another digital with payoff $X_2(T)=1$ if $S^2(T)>K$, $0$ otherwise, with $K=1.69$. Find $S_{X_2}(0)$. Is it larger or smaller than the price of Point 2?

> **Solution.** $S^2(T)>1.69\iff S(T)>1.3$ ⇒ $S_{X_2}(0)=e^{-0.2}N\Big(\frac{\ln\frac1{1.3}+0.02}{0.6}\Big)=0.81873\,N(-0.4039)$ — **larger** (lower threshold).

**5.** *(4 points)* Find the NA price of the derivative of Point 4 for any $t\in(0,T)$.

> **Solution.** $S_{X_2}(t)=e^{-r(T-t)}N\Big(\frac{\ln\frac{S(t)}{1.3}+(r-\frac{\sigma^2}{2})(T-t)}{\sigma\sqrt{T-t}}\Big)$.

**6.** *(4 points)* Is the replicating strategy of the derivative of Point 4 long or short on $S$?

> **Solution.** The price is increasing in $S(t)$ ⇒ $\vartheta_1>0$: **long**.

**7.** *(6 points)* Compute $P[X_2(T)>X_1(T)]$.

> **Solution.** Happens iff $1.3<S(T)\le1.69$: $P=N\Big(\frac{\ln\frac{1}{1.3}+0.18}{0.6}\Big)-N\Big(\frac{\ln\frac{1}{1.69}+0.18}{0.6}\Big)=N(-0.1373)-N(-0.5746)\approx0.162$.

### [Jan 13, 2025] Exercise 2 (40 points)

**Text.** $S(0)=10$, $r=6\%$, $\mu=8\%$, $\sigma=25\%$, $T=4$.

**1.** *(7 points)* Compute the historical probability that a European call with maturity $T$ and strike $K=10$ closes in the money. Is it larger or smaller than 50%?

> **Solution.** $P[S(T)>10]=N\big(\frac{(\mu-\frac{\sigma^2}2)\sqrt T}{\sigma}\big)=N(0.39)>50\%$.

**2.** *(6 points)* Compute $\mathbb{E}^Q[S(T)^3]$. (You may use $\mathbb{E}[e^{N(a,b^2)}]=e^{a+b^2/2}$.)

> **Solution.** $\mathbb{E}^Q[S(T)^3]=S_0^3e^{3(r-\frac{\sigma^2}2)T+\frac92\sigma^2T}=S_0^3e^{3rT+3\sigma^2T}=1000e^{1.47}=$ **4349.2**.

**3.** *(5 points)* Compute $S_Y(0)$, the NA price at $t=0$ of the derivative with payoff $Y(T)=S(T)^3$.

> **Solution.** $S_Y(0)=e^{-rT}\mathbb{E}^Q[S(T)^3]=S_0^3e^{2rT+3\sigma^2T}=1000e^{1.23}=$ **3421.2**.

**4.** *(5 points)* Find the replicating strategy $\vartheta(0)=(\vartheta_0(0),\vartheta_1(0))$ at $t=0$.

> **Solution.** $\vartheta_1(0)=3S_0^2e^{2rT+3\sigma^2T}=$ **1026.4**; $\vartheta_0(0)=S_Y(0)-\vartheta_1(0)S_0=-2S_0^3e^{1.23}=$ **$-6842.5$**.

**5.** *(8 points)* Compute the RN probabilities of the events $S(T)<S(0)$ and $S(T)<2S(0)$.

> **Solution.** $Q[S(T)<S_0]=N\big(-\frac{(r-\frac{\sigma^2}{2})\sqrt T}{\sigma}\big)=N(-0.23)$; $Q[S(T)<2S_0]=N\big(\frac{\ln2-(r-\frac{\sigma^2}2)T}{\sigma\sqrt T}\big)=N(1.1563)$.

**6.** *(5 points)* Consider the European derivative with payoff $X(T)=0$ if $S(T)<S(0)$, $1$ if $S(0)\le S(T)<2S(0)$, $2$ if $S(T)\ge2S(0)$. Compute $S_X(0)$.

> **Solution.** $X=\mathbf 1_{\{S(T)\ge S_0\}}+\mathbf 1_{\{S(T)\ge2S_0\}}$ ⇒ $S_X(0)=e^{-rT}\big(2-N(-0.23)-N(1.1563)\big)\approx0.562$.

**7.** *(4 points)* Compute the price of the previous derivative at any $t\in(0,T)$.

> **Solution.** $S_X(t)=e^{-r(T-t)}\big[N(d_2(S_0))+N(d_2(2S_0))\big]$, with $d_2(K)=\frac{\ln\frac{S(t)}{K}+(r-\frac{\sigma^2}2)(T-t)}{\sigma\sqrt{T-t}}$.

### [Jan 29, 2025] Exercise 2 (40 points)

**Text.** $S(0)=1$, $r=5\%$, $\mu=9\%$, $\sigma=25\%$, $T=2$.

**1.** *(7 points)* Compute the RN probability that a European call with maturity $T$ and strike $K=1$ closes in the money. Is it larger or smaller than 50%?

> **Solution.** $Q[S(T)>1]=N\big(\frac{(r-\frac{\sigma^2}2)\sqrt T}{\sigma}\big)=N(0.10607)>50\%$.

**2.** *(5 points)* Compute $\mathbb{E}^Q[S(T)^2]$.

> **Solution.** $S_0^2e^{(2r+\sigma^2)T}=e^{0.325}=$ **1.384**.

**3.** *(6 points)* Consider the derivative with payoff $Y(T)=S(T)^2e^{\alpha T}$, $\alpha\in\mathbb{R}$. Compute $S_Y(0)$ in terms of $\alpha$.

> **Solution.** $S_Y(0)=e^{-rT}e^{\alpha T}\mathbb{E}^Q[S(T)^2]=S_0^2e^{(\alpha+r+\sigma^2)T}=e^{2\alpha+0.225}$.

**4.** *(3 points)* Find $\alpha$ such that $S_Y(0)=S(0)$.

> **Solution.** $2\alpha+0.225=0$ ⇒ **$\alpha=-0.1125$**.

**5.** *(5 points)* Find the replicating strategy $\vartheta(0)$ at $t=0$ (with this $\alpha$).

> **Solution.** $\vartheta_1(0)=2S_0e^{(\alpha+r+\sigma^2)T}=$ **2**, $\vartheta_0(0)=S_Y(0)-2S_0=$ **$-1$**.

**6.** *(6 points)* Compute $\mathbb{E}^Q[S(2)\mid\mathcal{F}_1]$. (Hint: $S(2)=S(1)\frac{S(2)}{S(1)}$.)

> **Solution.** $S(2)=S(1)e^{(r-\frac{\sigma^2}2)+\sigma(W^Q(2)-W^Q(1))}$, with the increment independent of $\mathcal{F}_1$ ⇒ $\mathbb{E}^Q[S(2)|\mathcal{F}_1]=S(1)e^{r}$.

**7.** *(3 points)* Consider the derivative with maturity 1 and payoff $X(1)=S(1)$ if $S(1)>b$, $0$ otherwise, with $b=1.5$. Show that $S_X(0)=S(0)N(d_1)$, where $d_1$ is that of a call with maturity 1 and strike $b$, and compute it.

> **Solution.** $X(1)=(S(1)-b)^++b\mathbf 1_{\{S(1)>b\}}$ ⇒ $S_X(0)=[S_0N(d_1)-be^{-r}N(d_2)]+be^{-r}N(d_2)=S_0N(d_1)$, with $d_1=\frac{\ln\frac{1}{1.5}+(0.05+0.03125)}{0.25}=-1.2969$ ⇒ $S_X(0)=N(-1.2969)\approx0.0973$.

**8.** *(5 points)* Consider the exotic barrier derivative with maturity $T=2$ and payoff $X_{ex}(2)=S(2)$ if $S(1)>b$, $0$ otherwise ($b=1.5$). Compute $S_{X_{ex}}(0)$.

> **Solution.** Tower property: $e^{-2r}\mathbb{E}^Q\big[\mathbf 1_{\{S(1)>b\}}\mathbb{E}^Q_1[S(2)]\big]=e^{-2r}\mathbb{E}^Q[\mathbf 1_{\{S(1)>b\}}S(1)e^r]=S_X(0)=$ **$N(-1.2969)$**. (Replication: buy $X$; at $t=1$, if paid, use $S(1)$ to buy one share and hold it.)

### [Dec 19, 2025] Exercise 2 (40 points)

**Text.** $S(0)=1$, $r=4\%$, $\mu=9\%$, $\sigma=20\%$, $T=10$.

**1.** *(5 points)* Compute the historical probability that a European call with maturity $T=10$ and strike $K=1$ closes in the money.

> **Solution.** $P[S(10)>1]=N\big(\frac{(\mu-\frac{\sigma^2}2)\sqrt{10}}{\sigma}\big)=N(1.1068)\approx0.866$.

**2.** *(7 points)* A European digital option with maturity $T=10$ pays 1 if $S(T)>K=1$ and 0 otherwise. Compute its initial NA price. Is it increasing or decreasing in $\sigma$?

> **Solution.** $e^{-rT}N(d_2)$ with $d_2=\frac{(r-\frac{\sigma^2}{2})\sqrt T}{\sigma}=0.3162$ ⇒ $e^{-0.4}N(0.316)=0.670\,N(0.316)$. Since $d_2=\frac{r\sqrt T}{\sigma}-\frac{\sigma\sqrt T}{2}$ decreases in $\sigma$, the price is **decreasing in $\sigma$**.

**3.** *(6 points)* A forward on $S$ with maturity $T_i$ obliges the holder to buy one unit of $S$ at $T_i$ for the delivery price $F_{0,T_i}$ agreed at $t=0$; the long payoff is $S(T_i)-F_{0,T_i}$ and $F_{0,T_i}$ makes the initial price zero. For $T_1=1$ and $T_2=5$ determine $F_{0,T_1}$ and $F_{0,T_2}$.

> **Solution.** $F_{0,T_i}=S(0)e^{rT_i}$: $F_{0,1}=e^{0.04}=1.0408$; $F_{0,5}=e^{0.2}=1.2214$.

**4.** *(6 points)* Consider the *forward calendar spread* $X$: a short position in the forward with maturity $T_1=1$ and a long position in the forward with maturity $T_2=5$. Determine its cashflow $X(t)$ for all $0\le t\le T_2$.

> **Solution.** $X(T_1)=F_{0,T_1}-S(T_1)$ at $T_1=1$; $X(T_2)=S(T_2)-F_{0,T_2}$ at $T_2=5$; zero at all other dates.

**5.** *(4 points)* Determine $V_X(0)$, its initial NA price.

> **Solution.** $V_X(0)=0$ (both forwards have zero initial value).

**6.** *(7 points)* Determine $V_X(t)$ for $T_1<t<T_2$.

> **Solution.** Only the long $T_2$-forward is alive: $V_X(t)=S(t)-F_{0,T_2}e^{-r(T_2-t)}=S(t)-S(0)e^{rt}$.

**7.** *(5 points)* Find the historical probability that $V_X(t)\ge0$ for $T_1<t<T_2$. Is it increasing or decreasing in $t$?

> **Solution.** $P[V_X(t)\ge0]=P\big[\ln\frac{S(t)}{S_0}\ge rt\big]=N\big(\frac{(\mu-\frac{\sigma^2}{2}-r)\sqrt t}{\sigma}\big)=N(0.15\sqrt t)$ — **increasing in $t$**.

### [Jan 2026] Exercise 2 (40 points)

**Text.** $S(0)=10$, $r=5\%$, $\mu=9\%$, $\sigma=25\%$, $T=4$. (Useful: $d_2=\frac{(r-\frac{\sigma^2}2)\sqrt T}{\sigma}=0.15$, $d_1=d_2+\sigma\sqrt T=0.65$, $e^{-rT}=0.8187$, for strike $10$.)

**1.** *(5 points)* Compute the risk-neutral probability that a European put with maturity $T=4$ and strike $K_1=10$ closes in the money.

> **Solution.** $Q[S(T)<K_1]=N(-d_2)=N(-0.15)$.

**2.** *(6 points)* Compute the initial price of a digital option with payoff $DO(T)=1$ if $S(T)<K_1=10$, $0$ otherwise.

> **Solution.** $e^{-rT}N(-d_2)=0.8187\,N(-0.15)$.

**3.** *(6 points)* Compute $p(0)$, the price at $t=0$ of a European put with maturity $T$ and strike $K_1=10$.

> **Solution.** $p(0)=K_1e^{-rT}N(-d_2)-S_0N(-d_1)=8.187\,N(-0.15)-10\,N(-0.65)$.

**4.** *(4 points)* A *gap put* has two strikes $K_1=10<K_2=20$: a trigger strike $K_1$ (whether it pays) and a payoff strike $K_2$ (how much): $X(T)=(K_2-S(T))^+$ if $S(T)<K_1$, $0$ otherwise. Determine $k$ such that $X(T)=k\,DO(T)+(K_1-S(T))^+$ and show that the equality holds.

> **Solution.** On $\{S<K_1\}$: $K_2-S=(K_1-S)+(K_2-K_1)$; on $\{S\ge K_1\}$ both sides are 0 ⇒ **$k=K_2-K_1=10$**.

**5.** *(5 points)* Determine $V_X(0)$, the initial NA price of the gap put.

> **Solution.** $V_X(0)=p(0)+10\cdot0.8187N(-0.15)=16.37\,N(-0.15)-10\,N(-0.65)$.

**6.** *(5 points)* Determine $V_X(t)$ for any $t<T$.

> **Solution.** $V_X(t)=K_2e^{-r(T-t)}N(-d_2(t))-S(t)N(-d_1(t))$, with $d_{1,2}(t)=\frac{\ln\frac{S(t)}{K_1}+(r\pm\frac{\sigma^2}2)(T-t)}{\sigma\sqrt{T-t}}$.

**7.** *(5 points)* Compute by how much, in historical expectation, the gap put payoff exceeds the standard put payoff: $\mathbb{E}^P[X(T)-(K_1-S(T))^+]$.

> **Solution.** $=10\,P[S(T)<10]=10\,N\big(-\frac{(\mu-\frac{\sigma^2}{2})\sqrt T}{\sigma}\big)=10\,N(-0.47)$.

**8.** *(4 points)* Suppose the strikes are inverted, $K_1=20>K_2=10$: $X(T)=(10-S(T))^+$ if $S(T)<20$, $0$ otherwise. Derive its initial price, justifying your answer.

> **Solution.** If $S<10$ then automatically $S<20$ ⇒ $X(T)=(10-S(T))^+$: a plain put with strike 10 ⇒ price $=p(0)=8.187N(-0.15)-10N(-0.65)$.
