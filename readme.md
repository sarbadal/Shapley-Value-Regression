<span style="color: #6F343F; font-family: Babas; font-size: 3em;">

# Shapley Value Regression

</span>

<span style="color: #666AE5; font-family: Babas; font-size: 2em;">

# Introduction:

In the econometric literature multicollinearity is defined as the incidence of
high degree of correlation among some or all regressor variables. Strong multicollinearity has
deleterious effects on the confidence intervals of linear regression coefficients (β in the linear
regression model y=Xβ+u). Although it does not affect the explanatory power ($R^2$) of the
regressors or unbiasedness of the estimated coefficients associated with them, it does inflate
their standard error of estimate rendering test of hypothesis misleading or paradoxical, often
such that although $R^2$ could be very high, individual coefficients may all have poor Student’s tvalues.
Thus, strong multicollinearity may lead to failure in rejecting a false null hypothesis of
ineffectiveness of the regressor variable to the regressand variable (type II error). Very
frequently, it also affects the sign of the regression coefficients. However, it has been pointed
out that the incidence of high degree of correlation (measured in terms of a large condition
number; Belsley et al., 1980) among some or all regressor variables alone (unsupported by large
variance of error in the regressand variable, y) has little effect on the precision of regression
coefficients. Large condition number coupled with a large variance of error in the regressand
variable destabilizes the regression estimator; either of the two in isolation cannot cause much
harm, although the condition number is relatively more potent in determining the stability of
estimated regression coefficients (Mishra, 2004-a).


### Shapley value regression:
> This is an entirely different strategy to assess the contribution of
regressor variables to the regressand variable. It owes its origin in the theory of cooperative
games (Shapley, 1953). The value of $R^2$ obtained by fitting a linear regression model y=Xβ+u is
considered as the value of a cooperative game played by X (whose members, xj ϵ X; j=1, m,
work in a coalition) against y (explaining it). The analyst does not have enough information to
disentangle the contributions made by the individual members xj ϵ X; j=1, m, but only their joint
1 contribution ($R^2$) is known. The Shapley value decomposition imputes the most likely
contribution of each individual xj ϵ X; j=1, m, to $R^2$.

### An algorithm to impute the contribution of individual variables to Shapley value:
>Let there be m number of regressor variables in the model y=Xβ+u. Let X(p, r) be the r-membered subset
of X in which the pth regressor appears and X(q, r) be the r-membered subset of X in which the
pth regressor does not appear. Further, let $R^2(p, r)$ be the $R^2$ obtained by regression of y on X(p,
r) and $R^2(q, r)$ be the $R^2$ obtained by regression of y on X(q, r). Then, the share of the regressor
variable p (that is xp ϵ X) is given by  $S(p) = (1/m)\left\{\sum_{i=1}^{m}[R^2(p,r) - R^2(q, r-1)]\right\}/k$.
Moreover, $R^2(q,0) = 0$. Here k is the number of cases in which the evaluation in [.] was carried
out. The sum of all S(p) for p=1, m (that is, $\sum_{p=1}^{m}(p)$ is the $R^2$ of y=Xβ+u : (all xj ϵ X) or the
total value of the game = 
$R^2 = \sum_{p=1}^{m}S(p) = \sum_{p=1}^{m}(1/m)\sum_{r=1}^{k}\left\{\sum_{c=1}^{k}[R^2(p,r)-R^2(q, r-1)]\right\}/k.$


### Computational details of share of x1 in $R^2$:

|r  | r-1 |x1 |x2 |x3 |x4 |$R^2$   |K   | operation   | values  | Sum/k     | Grand value |
|---|:----|:--|:--|:--|:--|:-------|:---|:------------|:--------|:----------|:-----------:|
|4  |     |1  |2  |3  |4  |0.98237 |    |plus         |+0.98237 |           |             |
|   |3    |   |2  |3  |4  |0.97282 |    |minus        |-0.97282 |           |             |
|   |     |   |   |   |   |        |k=1 |Sum/k        |         |0.009556   |             |
|3  |     |1  |2  |3  |   |0.98228 |    |plus         |+0.98228 |           |             |
|3  |     |1  |2  |   |4  |0.98233 |    |plus         |+0.98233 |           |             |
|3  |     |1  |   |3  |4  |0.98128 |    |plus         |+0.98128 |           |             |
|   |2    |   |2  |3  |   |0.84702 |    |minus        |-0.84702 |           |             |
|   |2    |   |2  |3  |   |0.68006 |    |minus        |-0.68006 |           |             |
|   |2    |   |2  |3  |   |0.93529 |    |minus        |-0.93529 |           |             |
|   |     |   |   |   |   |        |k=3 |Sum/k        |         |0.161175   |             |
|2  |     |1  |2  |   |   |0.97867 |    |plus         |+0.97867 |           |             |
|2  |     |1  |   |3  |   |0.54816 |    |plus         |+0.54816 |           |             |
|2  |     |1  |   |   |4  |0.97247 |    |plus         |+0.97247 |           |             |
|   |1    |   |2  |   |   |0.66626 |    |minus        |-0.66626 |           |             |
|   |1    |   |   |3  |   |0.28587 |    |minus        |-0.28587 |           |             |
|   |1    |   |   |   |4  |0.67454 |    |minus        |-0.67454 |           |             |
|   |     |   |   |   |   |        |k=3 |Sum/k        |         |0.290878   |             |
|1  |     |1  |   |   |   |0.53394 |    |plus         |+0.53394 |           |             |
|   |     |   |   |   |   |        |k=1 |Sum/k        |         |0.533948   |             |
|   |     |   |   |   |   |        |    |Sum(sum/k)/m |         |           |**0.248889** |



</span>

$` \frac{n!}{k!(n-k)!} = {n \choose k} `$

$`\sqrt{2}`$











