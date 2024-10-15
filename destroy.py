import sh
import glob
import pandas as pd
from scipy.interpolate import interp1d
import numpy as np

df2 = pd.read_csv('21_04_2020_11_42_49_5559.csv',index_col='time',parse_dates=True)

df=df2.iloc[:6001]
print(df.shape)

df.to_csv('21_04_2020_11_42_49_5559.csv', index=True)
