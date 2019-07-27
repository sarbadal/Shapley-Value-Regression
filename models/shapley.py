"""
An algorithm to impute the contribution of individual variables to Shapley value:

Let there be m number of regressor variables in the model y=Xβ+u. Let X(p, r) be the r-membered subset
of X in which the pth regressor appears and X(q, r) be the r-membered subset of X in which the
pth regressor does not appear. Further, let R2(p, r) be the R2 obtained by
regression of y on X(p,r) and R2(q, r) be the R2 obtained by regression of y on X(q, r).
"""


import os
import itertools
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import r2_score


class ShapleyValue:

    def __init__(self, df, X, y):
        self.df = df
        self.__X = self._validate_x(X)
        self.__y = self._validate_y(y)


    @property
    def X(self):
        return self.__X

    def _validate_x(self, X):
        """Validate if all x numeric"""
        try:
            for x in self.df[X]:
                self.df[x] = self.df[x].astype(float)
            return X
        except:
            raise ValueError('All X columns must be numeric type')

    @property
    def y(self):
        return self.__y

    def _validate_y(self, y):
        """Validate if y variable is numeric"""
        try:
            self.df[y] = self.df[y].astype(float)
            return y
        except:
            raise ValueError('Y variable must be numeric type')

    def _get_r2(self, df_X, df_y):

        regr = linear_model.LinearRegression()
        regr.fit(df_X, df_y)
        y_hat = regr.predict(df_X)

        return r2_score(df_y, y_hat)


    def get_shapley_contribution(self, verbose=True, allvar=True):
        """
        Given data, X and y; it calculates the contribution of each regressor.
        """
        if verbose:
            print('+--Share of Individual Regressors and the Shapley Value--+')
            print('+--------------------------------------------------------+')

        ShareofIndividualRegressors = pd.DataFrame()
        ShareofIndividualRegressors['Regressor'] = ['Share']

        total = 0
        for x in self.X:
            c = self.get_shapley_contribution_of(x, verbose=verbose, allvar=allvar)[0]
            ShareofIndividualRegressors[x] = [c]
            total += c

        ShareofIndividualRegressors['Total'] = [total]

        if verbose:
            print('')
            print('+--End of Calculation--+')

        return ShareofIndividualRegressors


    def get_shapley_contribution_of(self, target_x, verbose=False, allvar=False):
        """
        It takes a list of words (or x variables) and creates
        a possible combination of x-var combi for regression.
        """
        out_df = pd.DataFrame()

        for i in range(len(self.X)):
            i_list = list(itertools.combinations(self.X, i + 1))

            for xcombo in i_list:
                if target_x in xcombo:

                    data_dict = dict()
                    for t in ['target', 'wt_target']:

                        if t == 'target':

                            data_dict['r'] = [i + 1]
                            data_dict['r-1'] = [i + 1 - 1]

                            for x in self.X:
                                data_dict[x] = [1] if x in xcombo else [0]

                            data_dict['R2'] = [self._get_r2(self.df[list(xcombo)], self.df[[self.y]])]


                        else:
                            xcombo_wt_target = [x for x in xcombo if x != target_x]

                            data_dict['r'].append(i + 1)
                            data_dict['r-1'].append(i + 1 - 1)

                            for x in self.X:
                                data_dict[x].append(1) if x in xcombo_wt_target else data_dict[x].append(0)

                            if len(xcombo_wt_target) == 0:
                                data_dict['R2'].append(0)
                            else:
                                data_dict['R2'].append(
                                    -self._get_r2(self.df[xcombo_wt_target], self.df[[self.y]])
                                )

                    out_df = pd.concat(
                        [out_df, pd.DataFrame(data_dict)],
                        axis=0,
                        ignore_index=True,
                        sort=False
                    )

        k = pd.DataFrame(out_df['r'].value_counts()).reset_index()
        k.rename(columns={'index': 'r', 'r': 'K'}, inplace=True)
        k['m'] = len(k)

        out_df = pd.merge(out_df, k, how='left', on='r')
        out_df['K'] /= 2
        out_df['values'] = out_df['R2'] / out_df['K']
        out_df['values'] /= out_df['m']

        contribution = out_df['values'].sum()
        total = self._get_r2(self.df[self.X], self.df[[self.y]])

        if verbose:
            if allvar:
                self._display(target_x=None, x=target_x, contribution=contribution, total=total)
            else:
                self._display(target_x=target_x, x=target_x, contribution=contribution, total=total)

        return contribution, out_df

    def _max_len_xvar(self):
        max_len = 0
        for x in self.X:
            max_len = len(x) if max_len < len(x) else max_len

        return max_len

    def _display(self, target_x=None, x=None, contribution=None, total=None):
        if target_x is None:
            max_len = self._max_len_xvar()
            printable_var = x if len(x) == max_len else x + ' ' * (max_len - len(x))
            print(f'+--R2 Share ({printable_var}): {round(contribution, 5)}\tof\t{round(total, 5)}--+')

        else:
            print(f'+--R2 Share ({x}): {round(contribution, 5)}\tof\t{round(total, 5)}--+')




if __name__ == '__main__':
    from settings.settings import DATA

    df = pd.read_csv(os.path.join(DATA, 'sample_data.csv'))

    sv = ShapleyValue(df, ['Impressions', 'Clk', 'Its a long Name'], 'y')
    # contribution = sv.get_shapley_contribution_of('Clk', verbose=True)[0]
    contribution_all = sv.get_shapley_contribution()

    # print(contribution)
    # print(contribution_all)


