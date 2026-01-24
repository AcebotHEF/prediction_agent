import pandas as pd
import numpy as np

def get_revenue_data():
    dates = pd.date_range(start="2023-01-01", periods=18, freq='M')
    revenue = [10000 + np.random.randint(-1000, 1500) + i*300 for i in range(len(dates))]
    df = pd.DataFrame({'Month': dates, 'Revenue': revenue})
    return df