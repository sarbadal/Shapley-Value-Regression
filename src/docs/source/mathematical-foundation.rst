.. _mathematical-foundation:

The Shapley Value Approach
==========================

Shapley Value Regression treats each predictor as a participant in a
cooperative game.

The total explanatory power of the model (typically measured using :math:`R^2`) is the
reward that must be distributed among all predictors.

For each predictor, the Shapley value asks:

On average, how much additional explanatory power does this predictor
contribute across all possible combinations of predictors?

Instead of evaluating a predictor in a single model specification, the method
evaluates its contribution across every possible subset of predictors and then
averages those contributions using a principled weighting scheme.

This produces a fair allocation of model explanatory power across all
predictors.


Advantages of Shapley Value Regression
--------------------------------------

Fair attribution of shared information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When predictors are correlated, several variables may carry similar
information. Shapley values distribute credit fairly among those variables,
rather than letting one predictor absorb most of the explanatory power.

Independence from variable ordering
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Many decomposition techniques depend on the order in which variables enter a
model. Shapley Value Regression evaluates all possible orderings and therefore
eliminates ordering bias.

Strong theoretical foundation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Shapley values satisfy several desirable properties:

- Efficiency: importance values sum exactly to the model's total explanatory
  power.
- Symmetry: predictors that contribute equally receive equal credit.
- Dummy property: predictors that provide no explanatory value receive zero
  importance.
- Additivity: importance values remain consistent when combining models.

Example (efficiency):

- Model :math:`R^2 = 0.75`
- Sum of all Shapley values = :math:`0.75`

These properties make Shapley values one of the most theoretically justified
methods for variable-importance decomposition.
