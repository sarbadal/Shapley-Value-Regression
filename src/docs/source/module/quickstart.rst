.. _quickstart:

🚀 Quickstart
=============

Example: Use as a package
-------------------------

Install locally in editable mode from the project root:

.. code-block:: bash

	pip install -e .

Then import and use the package in Python:

.. code-block:: python

	from shapley import ShapleyValue
	from shapley.data.load import get_dataset_info, load_dataset

	dataset_key = "death_rate"

	info = get_dataset_info(dataset_key)
	df = load_dataset(dataset_key)

	sv = ShapleyValue(df, info["default_X"], info["target"])
	contributions = sv.get_shapley_contribution(verbose=False)

	print(contributions)

Expected output format:

.. code-block:: text

	Regressor                                      Share
	lower_95_confidence_interval_for_death_rate    <float>
	upper_95_confidence_interval_for_death_rate    <float>
	recent_5_year_trend_2_in_death_rates           <float>
	average_deaths_per_year                        <float>
	Total                                          <float>

Get contribution for a single regressor:

.. code-block:: python

	contribution, details = sv.get_shapley_contribution_of("average_deaths_per_year")
	print(contribution)
	print(details.head())

Available packaged datasets:

* ``death_rate``
* ``distance_metro``

Example: Use your own pandas DataFrame
--------------------------------------

You can also pass your own DataFrame directly, as long as selected feature columns and target column are numeric.

.. code-block:: python

	import pandas as pd

	from shapley import ShapleyValue

	# User-provided dataset
	df = pd.DataFrame(
	  {
	    "sq_feet": [950, 1100, 1300, 1600, 1800, 2100],
	    "age_years": [20, 15, 12, 10, 8, 5],
	    "bedrooms": [2, 2, 3, 3, 4, 4],
	    "distance_km": [8.0, 7.2, 6.5, 5.0, 4.0, 3.0],
	    "price_usd": [220000, 250000, 290000, 340000, 390000, 450000],
	  }
	)

	X = ["sq_feet", "age_years", "bedrooms", "distance_km"]
	y = "price_usd"

	sv = ShapleyValue(df, X, y)

	# All feature contributions
	contributions = sv.get_shapley_contribution(verbose=False)
	print(contributions)

	# Single feature contribution and detailed intermediate table
	sq_feet_share, sq_feet_details = sv.get_shapley_contribution_of("sq_feet")
	print("sq_feet share:", sq_feet_share)
	print(sq_feet_details.head())

- :ref:`Class Reference <class_shapley_value_regression>`
- :ref:`Back to Home <home>`

