.. _shapley-value-regression:

Why Shapley Value Regression
============================

When building a regression model, one of the most common questions is:

Which predictors are most important in explaining or predicting the target
variable?

A common approach is to examine:

- regression coefficients (beta values)
- standardized coefficients
- correlations
- sequential changes in :math:`R^2`

These methods are computationally inexpensive and easy to interpret, but they
can become misleading when predictors are correlated or share explanatory
information.

Shapley Value Regression provides an alternative perspective by allocating model
explanatory power among predictors using principles from cooperative game
theory.

Shapley value regression
------------------------

Shapley Value Regression is a different strategy for assessing the contribution
of regressor variables to the target variable. It originates from cooperative
game theory (Shapley, 1953).

In this framing, the :math:`R^2` from the linear model
:math:`y = X\beta + u` is treated as the total value of a cooperative game.
The predictors in :math:`X` are the players, and their individual
contributions are imputed from the observed joint explanatory power.


An algorithm to impute individual contributions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let there be ``m`` regressors in the model :math:`y = X\beta + u`.

- Let :math:`X(p, r)` be an ``r``-member subset of :math:`X` that contains
  regressor ``p``.
- Let :math:`X(q, r)` be an ``r``-member subset of :math:`X` that does not
  contain regressor ``p``.
- Let :math:`R^2(p, r)` be the :math:`R^2` from regressing :math:`y` on
  :math:`X(p, r)`.
- Let :math:`R^2(q, r)` be the :math:`R^2` from regressing :math:`y` on
  :math:`X(q, r)`.

Then, the share of regressor ``p`` (that is, :math:`x_p \in X`) is:

.. math::

   S(p) = \frac{1}{m}\frac{\sum_{i=1}^{m}\left[R^2(p,r)-R^2(q,r-1)\right]}{k}

with :math:`R^2(q, 0) = 0`, and ``k`` equal to the number of evaluated cases.

The sum of all shares equals total model explanatory power:

.. math::

   R^2 = \sum_{p=1}^{m} S(p)


Computational details of share of :math:`X_j` in :math:`R^2`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For each regressor, computation proceeds by comparing:

- models that include the regressor ("plus" terms), and
- matched models that exclude it ("minus" terms),

across subset sizes, followed by averaging within each subset size and then
across all sizes.

.. csv-table:: Worked example for a focal regressor
  :header: "r", "r-1", "x1", "x2", "x3", "x4", ":math:`R^2`", "K", "operation", "values", "Sum/k", "Grand value"

  "4", "", "1", "2", "3", "4", "0.98237", "", "plus", "+0.98237", "", ""
  "", "3", "", "2", "3", "4", "0.97282", "", "minus", "-0.97282", "", ""
  "", "", "", "", "", "", "", "k=1", "Sum/k", "", "0.009556", ""
  "3", "", "1", "2", "3", "", "0.98228", "", "plus", "+0.98228", "", ""
  "3", "", "1", "2", "", "4", "0.98233", "", "plus", "+0.98233", "", ""
  "3", "", "1", "", "3", "4", "0.98128", "", "plus", "+0.98128", "", ""
  "", "2", "", "2", "3", "", "0.84702", "", "minus", "-0.84702", "", ""
  "", "2", "", "2", "", "4", "0.68006", "", "minus", "-0.68006", "", ""
  "", "2", "", "", "3", "4", "0.93529", "", "minus", "-0.93529", "", ""
  "", "", "", "", "", "", "", "k=3", "Sum/k", "", "0.161175", ""
  "2", "", "1", "2", "", "", "0.97867", "", "plus", "+0.97867", "", ""
  "2", "", "1", "", "3", "", "0.54816", "", "plus", "+0.54816", "", ""
  "2", "", "1", "", "", "4", "0.97247", "", "plus", "+0.97247", "", ""
  "", "1", "", "2", "", "", "0.66626", "", "minus", "-0.66626", "", ""
  "", "1", "", "", "3", "", "0.28587", "", "minus", "-0.28587", "", ""
  "", "1", "", "", "", "4", "0.67454", "", "minus", "-0.67454", "", ""
  "", "", "", "", "", "", "", "k=3", "Sum/k", "", "0.290878", ""
  "1", "", "1", "", "", "", "0.53394", "", "plus", "+0.53394", "", ""
  "", "", "", "", "", "", "", "k=1", "Sum/k", "", "0.533948", ""
  "", "", "", "", "", "", "", "", "Sum(sum/k)/m", "", "", "0.248889"

In this 4-variable example, the final average share for the focal variable is
``0.248889``.

For scalability implications of this enumeration strategy, see
:doc:`computational-considerations`.

