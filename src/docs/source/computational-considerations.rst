.. _computational-considerations:

Computational Considerations
============================

This section summarizes the expected execution time of the
``ShapleyValue`` class as the number of regressors increases.


Runtime Growth
--------------

Let:

- :math:`m` = number of regressors (``len(X)``)
- :math:`t_{fit}` = average time to run one linear regression fit, prediction, and
  :math:`R^2` calculation

The implementation computes Shapley contribution for each regressor by
evaluating all subsets that include that regressor.

- For one target regressor: regression fits = :math:`2^m`
- For all regressors: regression fits = :math:`m * 2^m`

So the dominant runtime is:

:math:`T(m) \sim m * 2^m * t_{fit}`

This is exponential in :math:`m`.


Estimated Execution Time by Number of X Variables
-------------------------------------------------

.. list-table::
   :header-rows: 1

   * - X vars (m)
     - Regression fits (:math:`m*2^m`)
     - Time if :math:`t_{fit} = 1 \text{ ms}`
     - Time if :math:`t_{fit} = 5 \text{ ms}`
   * - 5
     - 160
     - 0.16 s
     - 0.80 s
   * - 8
     - 2,048
     - 2.05 s
     - 10.24 s
   * - 10
     - 10,240
     - 10.24 s
     - 51.2 s
   * - 12
     - 49,152
     - 49.2 s
     - 4.10 min
   * - 14
     - 229,376
     - 3.82 min
     - 19.1 min
   * - 15
     - 491,520
     - 8.19 min
     - 41.0 min
   * - 16
     - 1,048,576
     - 17.5 min
     - 87.4 min
   * - 18
     - 4,718,592
     - 78.6 min
     - 6.55 h
   * - 20
     - 20,971,520
     - 5.83 h
     - 29.1 h


Practical Interpretation
------------------------

- Up to about 10 to 12 variables is usually manageable on a typical laptop.
- Around 14 to 16 variables becomes expensive.
- 18 or more variables can be very slow unless fits are extremely fast or work
  is parallelized or approximated.


Notes
-----

- Actual runtime depends on row count :math:`n`, feature scaling, BLAS/LAPACK
  performance, and hardware.
- In this implementation, repeated fits on overlapping subsets are not cached,
  so measured times can vary, but the growth trend remains exponential.

- :ref:`Class Reference <class_shapley_value_regression>`
- :ref:`Back to Home <home>`
