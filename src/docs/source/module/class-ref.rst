.. _class_shapley_value_regression:

.. currentmodule:: shapley.models.shapley

✎ᝰ ShapleyValue Class
======================

The ``ShapleyValue`` class is the main interface for computing Shapley values 
for regression problems. It takes a pandas DataFrame, a list of feature column names, 
and a target column name as input, and provides methods to compute the Shapley 
contributions of each feature to the target variable.

Class Reference
---------------

.. py:class:: ShapleyValue(df: pd.DataFrame, feature_cols: List[str], target_col: str)

   Initializes the ShapleyValue object.

   :param df: A pandas DataFrame containing the dataset.
   :param feature_cols: A list of column names in the DataFrame to be used as features.
   :param target_col: The name of the column in the DataFrame to be used as the target variable.

.. py:method:: get_shapley_contribution(verbose: bool = True) -> pd.DataFrame
    Computes the Shapley contributions of each feature to the target variable.
    
    :param verbose: If True, prints progress information during computation.
    :return: A pandas DataFrame containing the Shapley contributions for each feature and a total contribution.

.. py:method:: get_shapley_contribution_of(feature_name: str) -> Tuple[float, pd.DataFrame]
    Computes the Shapley contribution of a single feature to the target variable.
    
    :param feature_name: The name of the feature for which to compute the Shapley contribution.
    :return: A tuple containing the Shapley contribution of the feature and a pandas DataFrame with detailed intermediate results.


Note
----

The ShapleyValue class is designed for regression problems where the target variable is continuous. 
It may not be suitable for classification problems or other types of machine learning tasks. 

- :ref:`Quickstart Guide <quickstart>`
- :ref:`Back to Home <home>`