import sh
import glob
import pandas as pd
from scipy.interpolate import interp1d
import numpy as np

df_csv_append = pd.DataFrame()
csv_files = glob.glob('21*.{}'.format('csv'))


for file in csv_files:    
    df2 = pd.read_csv(file)
    df2.drop_duplicates(subset=['time'], keep='first')
    df2.to_csv(file, index=False)
