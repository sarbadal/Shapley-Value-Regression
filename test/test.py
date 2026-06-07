import unittest
import pandas as pd
from pathlib import Path

from shapley import ShapleyValue

_DATA_DIR = Path(__file__).resolve().parent / 'data'
_DISTANCE_FILE = 'Distance_Metro_KM.csv'
_DEATH_FILE = 'death.csv'


class BaseShapleyValue(unittest.TestCase):
    filename: Path = None
    expected_columns: set = None
    features: list = None
    target: str = None

    @classmethod
    def setUpClass(cls) -> None:
        if cls.filename is None:
            raise unittest.SkipTest("Base test class; configure filename in subclass")
        cls.csv_path = _DATA_DIR / cls.filename
        cls.df = pd.read_csv(cls.csv_path)

    def test_csv_has_expected_columns(self) -> None:
        self.assertTrue(self.expected_columns.issubset(set(self.df.columns)))

    def test_get_shapley_contribution_returns_expected_table(self) -> None:
        sv = ShapleyValue(self.df, self.features, self.target)

        contribution_table = sv.get_shapley_contribution(verbose=False)
        print(contribution_table)

        expected_columns = ['Regressor', 'Share']
        self.assertListEqual(list(contribution_table.columns), expected_columns)

        expected_regressors = set(self.features + ['Total'])
        self.assertSetEqual(set(contribution_table['Regressor']), expected_regressors)

        total_share = float(contribution_table.loc[contribution_table['Regressor'] == 'Total', 'Share'].iloc[0])
        full_model_r2 = sv._get_r2(sv.df[self.features], sv.df[[self.target]])

        self.assertAlmostEqual(total_share, full_model_r2, places=6)

    def test_get_shapley_contribution_of_returns_expected_outputs(self) -> None:
        sv = ShapleyValue(self.df, self.features, self.target)

        contribution, details_df = sv.get_shapley_contribution_of('Distance_Metro_KM', verbose=False)

        self.assertIsInstance(contribution, float)
        self.assertFalse(details_df.empty)
        self.assertIn('values', details_df.columns)
        self.assertAlmostEqual(contribution, float(details_df['values'].sum()), places=10)

    def test_unknown_target_feature_raises(self) -> None:
        sv = ShapleyValue(self.df, self.features, self.target)

        with self.assertRaises(ValueError):
            sv.get_shapley_contribution_of('Not_A_Column', verbose=False)

    def test_non_numeric_feature_raises(self) -> None:
        bad_df = self.df.copy()
        bad_df = bad_df.astype({"Distance_Metro_KM": "object"})
        bad_df.loc[0, "Distance_Metro_KM"] = "not-a-number"

        with self.assertRaises(ValueError):
            ShapleyValue(bad_df, self.features, self.target)


class TestShapleyValueWithDistanceMetroData(BaseShapleyValue):
    filename = _DISTANCE_FILE
    expected_columns = {'Property_ID', 'Sq_Feet', 'Age_Yrs', 'Bedrooms', 'Distance_Metro_KM', 'Floors', 'Price_USD'}
    features = ['Sq_Feet', 'Age_Yrs', 'Bedrooms', 'Distance_Metro_KM', 'Floors']
    target = 'Price_USD'

"""
class TestShapleyValueWithDeathData(BaseShapleyValue):
    filename = _DEATH_FILE
    expected_columns = {
        'county',
        'fips',
        'met_objective_of_45_5_1',
        'age_adjusted_death_rate',
        'lower_95_confidence_interval_for_death_rate',
        'upper_95_confidence_interval_for_death_rate',
        'average_deaths_per_year',
        'recent_trend_2',
        'recent_5_year_trend_2_in_death_rates',
        'lower_95_confidence_interval_for_trend',
        'upper_95_confidence_interval_for_trend',
    }
    features = [
        'lower_95_confidence_interval_for_death_rate',
        'upper_95_confidence_interval_for_death_rate',
        'recent_5_year_trend_2_in_death_rates',
        'average_deaths_per_year',
    ]
    target = 'age_adjusted_death_rate'
"""


if __name__ == '__main__':
    unittest.main()
