import os
import pandas as pd
from models.shapley import ShapleyValue
from settings.settings import DATA

df = pd.read_csv(os.path.join(DATA, 'natural_gas.csv'))

sv = ShapleyValue(df, [
            'Cooling Degree Days',
            'Heating Degree Days',
            'Mean Maximum Temp',
            'Mean MinimumTemp',
            'Mean Temp',
        ],
        '_Total NC Natural Gas '
)
# contribution = sv.get_shapley_contribution_of('Clk', verbose=True)[0]
contribution_all = sv.get_shapley_contribution()

# print(contribution)
print(contribution_all)