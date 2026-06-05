import pandas as pd
from pathlib import Path

from models.shapley import ShapleyValue

CSV_FILE = Path(__file__).resolve().parent / 'test/data/Distance_Metro_KM.csv'

def main() -> None:
    df = pd.read_csv(CSV_FILE)
    features = ['Sq_Feet', 'Age_Yrs', 'Bedrooms', 'Distance_Metro_KM', 'Floors']
    target = 'Price_USD'
    
    sv = ShapleyValue(df, features, target)
    contribution_all = sv.get_shapley_contribution()
    print(contribution_all)


if __name__ == '__main__':
    main()