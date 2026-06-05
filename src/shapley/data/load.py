from pathlib import Path
from typing import Any, Dict, List, Union

import numpy as np
import pandas as pd


DATA_DIR = Path(__file__).resolve().parent
DISTANCE_METRO_CSV = DATA_DIR / "Distance_Metro_KM.csv"
DEATH_CSV = DATA_DIR / "death.csv"


DATASET_CATALOG: Dict[str, Dict[str, Any]] = {
	"distance_metro": {
		"description": (
			"Residential property pricing dataset with floor area, age, bedroom count, "
			"distance to metro, and floor count as predictors for sale price."
		),
		"path": DISTANCE_METRO_CSV,
		"default_X": ["Sq_Feet", "Age_Yrs", "Bedrooms", "Distance_Metro_KM", "Floors"],
		"target": "Price_USD",
		"loader": "load_distance_metro_data",
	},
	"death_rate": {
		"description": (
			"Public-health mortality dataset cleaned to numeric columns, useful for "
			"modeling age-adjusted death rate using confidence intervals, trend, and "
			"average deaths per year."
		),
		"path": DEATH_CSV,
		"default_X": [
			"lower_95_confidence_interval_for_death_rate",
			"upper_95_confidence_interval_for_death_rate",
			"recent_5_year_trend_2_in_death_rates",
			"average_deaths_per_year",
		],
		"target": "age_adjusted_death_rate",
		"loader": "load_death_data",
	},
}


def load_csv(path: Union[str, Path], **kwargs) -> pd.DataFrame:
	"""Load a CSV file into a pandas DataFrame."""
	return pd.read_csv(Path(path), **kwargs)


def load_distance_metro_data() -> pd.DataFrame:
	"""Load the Distance_Metro_KM dataset."""
	return load_csv(DISTANCE_METRO_CSV)


def load_death_data() -> pd.DataFrame:
	"""Load and clean the death-rate dataset for regression use."""
	df = load_csv(DEATH_CSV)
	df = df.replace("**", np.nan)
	df["average_deaths_per_year"] = (
		df["average_deaths_per_year"]
		.astype(str)
		.str.replace(",", "", regex=False)
	)

	cols = [
		"age_adjusted_death_rate",
		"lower_95_confidence_interval_for_death_rate",
		"upper_95_confidence_interval_for_death_rate",
		"recent_5_year_trend_2_in_death_rates",
		"average_deaths_per_year",
	]
	return df[cols].apply(pd.to_numeric, errors="coerce").dropna()


def get_available_datasets() -> List[str]:
	"""Return the list of dataset keys available in this package."""
	return list(DATASET_CATALOG.keys())


def get_dataset_info(dataset_name: str) -> Dict[str, Any]:
	"""Return dataset description, path, defaults, and loader for a dataset key."""
	if dataset_name not in DATASET_CATALOG:
		raise ValueError(
			f"Unknown dataset '{dataset_name}'. Available datasets: {', '.join(get_available_datasets())}"
		)

	info = DATASET_CATALOG[dataset_name]
	return {
		"name": dataset_name,
		"description": info["description"],
		"path": str(info["path"]),
		"default_X": list(info["default_X"]),
		"target": info["target"],
		"loader": info["loader"],
	}


def load_dataset(dataset_name: str) -> pd.DataFrame:
	"""Load a dataset by key from the dataset catalog."""
	if dataset_name == "distance_metro":
		return load_distance_metro_data()
	if dataset_name == "death_rate":
		return load_death_data()

	raise ValueError(
		f"Unknown dataset '{dataset_name}'. Available datasets: {', '.join(get_available_datasets())}"
	)


__all__ = [
	"DATA_DIR",
	"DISTANCE_METRO_CSV",
	"DEATH_CSV",
	"load_csv",
	"load_distance_metro_data",
	"load_death_data",
	"DATASET_CATALOG",
	"get_available_datasets",
	"get_dataset_info",
	"load_dataset",
]
