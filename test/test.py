import unittest
import pandas as pd
from pathlib import Path

from models.shapley import ShapleyValue

_DATA_DIR = Path(__file__).resolve().parent / 'data'
_FILENAME = 'Distance_Metro_KM.csv'


class TestShapleyValueWithDistanceMetroData(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.csv_path = _DATA_DIR / _FILENAME
        cls.df = pd.read_csv(cls.csv_path)
        cls.features = ['Sq_Feet', 'Age_Yrs', 'Bedrooms', 'Distance_Metro_KM', 'Floors']
        cls.target = 'Price_USD'

    def test_csv_has_expected_columns(self) -> None:
        expected_columns = {'Property_ID', 'Sq_Feet', 'Age_Yrs', 'Bedrooms', 'Distance_Metro_KM', 'Floors', 'Price_USD'}
        self.assertTrue(expected_columns.issubset(set(self.df.columns)))

    def test_get_shapley_contribution_returns_expected_table(self) -> None:
        sv = ShapleyValue(self.df, self.features, self.target)

        contribution_table = sv.get_shapley_contribution(verbose=False)
        print(contribution_table)

        expected_columns = ['Regressor', *self.features, 'Total']
        self.assertListEqual(list(contribution_table.columns), expected_columns)
        self.assertEqual(contribution_table.loc[0, 'Regressor'], 'Share')

        total_share = float(contribution_table.loc[0, 'Total'])
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


if __name__ == '__main__':
    unittest.main()
