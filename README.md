# Markowitz-Model-Modern-Portfolio-Theory

A command line application where you can input your stock portfolio and do Markowitz portfolio analysis on it.
NOTE: Markowitz portfolio analysis can't be run on short positions.


Markowitz Model Assumptions
1. Returns are normally distributed with µ mean and σ standard deviation.
2. Investors are risk averse. More risk for more return.


**Statistics concepts revision which are useful for the model:**
X, Y = Random variables with finite outcomes and probabilities
x, y = Data values in X and Y respectively

1. Expected value (or mean). E[x] 
2. Variance (σ^2): Expected value of squared deviations of variables from mean. Variance = E[(x-mean(X)^2)]
3. Standard deviation (σ): Square root(variance) 
4. Covariance: Measure of joint variability of two random variables. Cov(x,y) = E[(x-mean(X))(y-mean(Y))]
NOTE: Issue with covariance is that: a. It's dimensional measure  b. It is not normalised so hard to compare datasets with large differences in spread.
5. Correlation: Dimensionless measure of how 2 variables more with respect to each other. Correlation(X,Y)=(E[(x-mean(X))(y-mean(Y))])/σ(x)*σ(y)
NOTE: It's value is always between -1 and +1. 
    >0 means positive relationship between variables, if one goes up the other goes up.
    =0 means no relationship between variables
    <0 means negative relationship between variables
6. Normal Distribution: Probability distribution (gaussian distribution) that is symmetric about the mean,
    showing data near mean are more frequent in occurrence. 
7. Sharpe Ratio: It's a risk return measure. Describes excess return for extra volatility that we endure holding riskier asset (stock).
S(x) = (r(x) - R(f))/σ(x)
r(x) = Average rate of return of investment x
R(f) = Rate of return of risk-free security
S(x) > 1 is considered to be good.

**Modern Portfolio Theory Recap**
MPT: Investors can construct optimal portfolios offering maximum possible expected return for level of risk. It's a portfolio optimization model.

1. Assists in selection of most efficient portfolio by considering various possible portfolios of given securities based on expected return (mean) and risk (variance).
2. Efficient Portfolio: Either highest return for a given risk, for lowest risk for given return.

Return:  (S(t+1)-S(t))/S(t)
Log daily returns: ln(S(t+1)/S(t))

Mathematical Formulation:
   Stock  Weights in Portfolio
1. Apple:  0.20
2. Google: 0.30
3. Tesla:  0.25
4. GE:     0.25

w(i): weight
r(i): return for 'i'th stock based on historical data
µ(i): Expecteed return for 'i'th asset or stock

µ(portfolio) = E[Σw(i)r(i)] = Σw(i)E[r(i)] = Σw(i)µ(i)
In matrix multiplication terms, Σw(i)µ(i) = w(transpose)*µ

σ(ij) = E[(r(i)-µ(i))(r(j)-µ(j))] < 0 means 2 stocks move inversely 
Need to calculate this between every pair. When i=j, variance=covariance

Reduce risk as much as possible. High positive covariance doesn't provide much diversification. Aim of diversification is to eliminate fluctuations in long term. 
Hence, we need uncorrelated stock.

σ(i)^2 = E[(r(i)-µ(i))^2]
For calculating variance, we need covariance matrix containing all the covariances of stocks involved in portfolio.

|σ(1)^2..........σ(1n)^2| = Σ 
|                       |
|                       |
.                       .
.                       .
|σ(n1)^2..........σ(n)^2|

σ(portfolio)^2 = E[(r(i)-µ(i))^2] = Σ(i)Σ(j)[w(i)w(j)σ(ij)] = w(transpose)Σw
Higher variance, higher risk.

Monte carlo simulation helps us with making decision.


