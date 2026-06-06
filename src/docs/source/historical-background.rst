.. _historical-background:

Historical Background
=====================

The idea behind Shapley Value Regression comes from *cooperative game theory*,
a branch of mathematics that studies how groups of participants work together
and how the resulting reward should be distributed.

The concept was introduced by `Lloyd Shapley <https://en.wikipedia.org/wiki/Lloyd_Shapley>`_ in 1953.

In cooperative games, several players contribute to a common objective. Once
that objective is achieved, a central question appears:

How should the total reward be fairly distributed among participants?

This is harder than it first seems, because value is often created by both
individual effort and collaboration.

For example, imagine three business partners jointly generating a profit of
$1,000,000. Determining how much of that outcome was produced by each person is
difficult, because part of the value is created only through cooperation.

Shapley's solution was mathematically rigorous and conceptually simple:

Measure each player's contribution when joining every possible coalition, then
average those contributions across all coalition orderings.

The resulting allocation is called the *Shapley value*.


From Cooperative Games to Regression Analysis
---------------------------------------------

Researchers later recognized that the same allocation problem appears in
statistical modeling.

In regression, predictors work together to explain variation in a target
variable. Just as players cooperate to generate a reward in a game, predictors
cooperate to generate explanatory power in a model.

This leads to an analogous question:

If multiple predictors jointly explain the target variable, how much credit
should each predictor receive?

The issue is especially important when predictors are correlated and share
information, for example:

- income and education
- age and work experience
- advertising spend and brand awareness

Traditional regression coefficients do not directly provide a fair allocation of
shared explanatory power. The Shapley framework addresses this gap.

By treating predictors as players and model performance as the reward, Shapley
values allocate explanatory power in a principled and interpretable way.


Analogy Between Game Theory and Regression
------------------------------------------

The mapping between cooperative game theory and regression is natural:

.. list-table::
   :header-rows: 1

   * - Cooperative game theory
     - Regression analysis
   * - Player
     - Predictor variable
   * - Coalition of players
     - Subset of predictors
   * - Reward
     - Model performance (typically :math:`R^2`)
   * - Player contribution
     - Predictor contribution
   * - Fair reward allocation
     - Variable-importance allocation

Under this interpretation, each predictor receives credit based on its average
contribution across all possible subsets of predictors.

This ensures variables are credited both for their standalone effect and for the
value they add through interaction with other predictors.


Why This Matters
----------------

Historically, the Shapley framework was not originally designed for statistics
or machine learning. It was developed to solve a fundamental fairness problem:

How should value be allocated when multiple contributors jointly create an
outcome?

Because variable importance in regression is fundamentally the same type of
allocation problem, the Shapley framework creates a strong bridge between game
theory and statistical modeling.

Today, Shapley-based methods are widely used in:

- regression analysis
- explainable artificial intelligence (XAI)
- feature attribution
- machine learning interpretation
- economic modeling
- risk analysis
- scientific research

More than seventy years after its introduction, the Shapley value remains one
of the most influential and theoretically grounded methods for attributing
contributions among cooperating participants, whether those participants are
players in a game or predictors in a statistical model.
 