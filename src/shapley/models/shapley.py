"""
An algorithm to impute the contribution of individual variables to Shapley value:

Let there be m number of regressor variables in the model y=Xβ+u. Let X(p, r) 
be the r-membered subset of X in which the pth regressor appears and X(q, r) be 
the r-membered subset of X in which the pth regressor does not appear. Further, 
let R2(p, r) be the R2 obtained by regression of y on X(p,r) and R2(q, r) be the 
R2 obtained by regression of y on X(q, r).
"""

import os
import itertools
from typing import Dict, Generator, List, Optional, Sequence, Tuple, TypedDict

import pandas as pd
from sklearn import linear_model
from sklearn.metrics import r2_score
from tabulate import tabulate


class ContributionRow(TypedDict):
    Regressor: str
    Share: float

class ShapleyValue:

    def __init__(self, df: pd.DataFrame, X: Sequence[str], y: str) -> None:
        self.df: pd.DataFrame = df.copy()
        self.__X: List[str] = self._validate_x(X)
        self.__y: str = self._validate_y(y)
        self.__r2_cache: Dict[Tuple[str, ...], float] = {}

    @property
    def X(self) -> List[str]:
        return self.__X

    def _cast_columns_to_float(self, columns: Sequence[str]) -> None:
        for column in columns:
            self.df[column] = self.df[column].astype(float)

    def _validate_x(self, X: Sequence[str]) -> List[str]:
        """Validate if all x numeric"""
        try:
            self._cast_columns_to_float(X)
            return list(X)
        except Exception as exc:
            raise ValueError('All X columns must be numeric type') from exc

    @property
    def y(self) -> str:
        return self.__y

    def _validate_y(self, y: str) -> str:
        """Validate if y variable is numeric"""
        try:
            self._cast_columns_to_float([y])
            return y
        except Exception as exc:
            raise ValueError('Y variable must be numeric type') from exc

    def _build_base_row(self, r: int, xcombo: Sequence[str]) -> Dict[str, float]:
        row: Dict[str, float] = {
            'r': r,
            'r-1': r - 1,
        }
        for x in self.X:
            row[x] = 1 if x in xcombo else 0
        return row

    def _build_target_rows(self, r: int, xcombo: Sequence[str], target_x: str) -> List[Dict[str, float]]:
        target_row = self._build_base_row(r, xcombo)
        target_row['R2'] = self._get_r2_for_columns(xcombo)

        xcombo_wt_target = [x for x in xcombo if x != target_x]
        wt_target_row = self._build_base_row(r, xcombo_wt_target)
        wt_target_row['R2'] = 0 if len(xcombo_wt_target) == 0 else -self._get_r2_for_columns(xcombo_wt_target)

        return [target_row, wt_target_row]

    def _iter_target_combinations(self, target_x: str) -> Generator[Tuple[int, Tuple[str, ...]], None, None]:
        for i in range(len(self.X)):
            for xcombo in itertools.combinations(self.X, i + 1):
                if target_x in xcombo:
                    yield i + 1, xcombo

    def _compute_shapley_values(self, out_df: pd.DataFrame) -> pd.DataFrame:
        k = out_df['r'].value_counts().rename_axis('r').reset_index(name='K')
        k['m'] = len(k)

        out_df = pd.merge(out_df, k, how='left', on='r')
        out_df['K'] /= 2
        out_df['values'] = out_df['R2'] / out_df['K']
        out_df['values'] /= out_df['m']

        return out_df

    def _calculate_contribution(self, out_df: pd.DataFrame) -> Tuple[float, float]:
        contribution: float = out_df['values'].sum()
        total: float = self._get_r2_for_columns(self.X)

        return contribution, total

    def _print_header(self) -> None:
        print('+--Share of Individual Regressors and the Shapley Value--+')
        print('+--------------------------------------------------------+')

    def _print_footer(self) -> None:
        print('')
        print('+--End of Calculation--+')

    def _build_contribution_table(self, contributions: Dict[str, float]) -> pd.DataFrame:
        rows: List[ContributionRow] = []
        total: float = 0

        for regressor, contribution in contributions.items():
            rows.append({'Regressor': regressor, 'Share': contribution})
            total += contribution

        rows.append({'Regressor': 'Total', 'Share': total})
        return pd.DataFrame(rows)

    def _get_contribution_for_regressor(self, x: str, verbose: bool, allvar: bool) -> float:
        return self.get_shapley_contribution_of(x, verbose=verbose, allvar=allvar)[0]

    def _validate_target_x(self, target_x: str) -> None:
        if target_x not in self.X:
            raise ValueError(f'{target_x} is not present in X')

    def _get_r2(self, df_X: pd.DataFrame, df_y: pd.DataFrame) -> float:
        regr = linear_model.LinearRegression()
        regr.fit(df_X, df_y)
        y_hat = regr.predict(df_X)

        return r2_score(df_y, y_hat)

    def _get_r2_for_columns(self, columns: Sequence[str]) -> float:
        key = tuple(columns)
        if key not in self.__r2_cache:
            self.__r2_cache[key] = self._get_r2(self.df[list(columns)], self.df[[self.y]])

        return self.__r2_cache[key]

    def get_shapley_contribution(self, verbose: bool = True, allvar: bool = True) -> pd.DataFrame:
        """
        Given data, X and y; it calculates the contribution of each regressor.
        """
        if verbose:
            self._print_header()

        contributions: Dict[str, float] = {}
        for x in self.X:
            contributions[x] = self._get_contribution_for_regressor(x, verbose=verbose, allvar=allvar)

        share_of_individual_regressors = self._build_contribution_table(contributions)

        if verbose:
            self._print_footer()

        return share_of_individual_regressors

    def get_shapley_contribution_of(self, target_x: str, verbose: bool = False, allvar: bool = False) -> Tuple[float, pd.DataFrame]:
        """
        It takes a list of words (or x variables) and creates
        a possible combination of x-var combi for regression.
        """
        self._validate_target_x(target_x)

        rows: List[Dict[str, float]] = []
        for r, xcombo in self._iter_target_combinations(target_x):
            rows.extend(self._build_target_rows(r, xcombo, target_x))

        out_df = pd.DataFrame(rows)
        out_df = self._compute_shapley_values(out_df)

        contribution, total = self._calculate_contribution(out_df)

        if verbose:
            if allvar:
                self._display(target_x=None, x=target_x, contribution=contribution, total=total)
            else:
                self._display(target_x=target_x, x=target_x, contribution=contribution, total=total)

        return contribution, out_df

    def _max_len_xvar(self) -> int:
        max_len: int = 0
        for x in self.X:
            max_len = len(x) if max_len < len(x) else max_len

        return max_len

    def _display(self, target_x: Optional[str] = None, x: Optional[str] = None, contribution: Optional[float] = None, total: Optional[float] = None) -> None:
        if x is None or contribution is None or total is None:
            return

        rows = [[x, round(contribution, 5), round(total, 5)]]
        headers = ['Regressor', 'R2 Share', 'Total R2']
        print(tabulate(rows, headers=headers, tablefmt='grid'))
