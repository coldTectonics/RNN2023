import sh
import glob
import pandas as pd
from scipy.interpolate import interp1d
import numpy as np

df = pd.read_csv('test.csv',index_col='time',parse_dates=True)

del df["image_name"]
del df["calib_status"]
del df["computer_time"]

df.to_csv('test.csv', index=True)
