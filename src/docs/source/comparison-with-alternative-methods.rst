.. _comparison-with-alternative-methods:

Comparison with Alternative Methods
===================================

.. list-table::
   :header-rows: 1
   :class: list-compact-table

   * - Method
     - Computational cost
     - Handles correlated predictors well
     - Fair attribution
   * - Regression coefficients
     - Very low
     - No
     - Limited
   * - Standardized coefficients
     - Very low
     - No
     - Limited
   * - Correlation analysis
     - Very low
     - No
     - Limited
   * - Sequential :math:`R^2` decomposition
     - Low
     - Partially
     - Order dependent
   * - Permutation importance
     - Moderate
     - Partially
     - Moderate
   * - Shapley Value Regression
     - High
     - Yes
     - Strong

Shapley Value Regression is often preferred when understanding variable
contribution is more important than computational efficiency.

When Alternative Methods May Be Preferable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Alternative methods may be more appropriate when:
 
- The dataset contains a large number of predictors.
- Computational resources are limited.
- Approximate importance estimates are sufficient.
- Real-time model interpretation is required.
 
In such cases, methods such as permutation importance, approximate SHAP algorithms, 
or other scalable feature attribution techniques may be more practical.

- :ref:`Class Reference <class_shapley_value_regression>`
- :ref:`Back to Home <home>`