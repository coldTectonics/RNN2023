import sh
import glob
import pandas as pd
from scipy.interpolate import interp1d
import numpy as np
from scipy.spatial.transform import Rotation as R
from scipy.spatial.transform import Slerp

df_csv_append = pd.DataFrame()
df = pd.DataFrame(columns=['image_name','hand_target_bin','paint_target_bin', 'computer_time', 'time', 'calib_status','rot_vec0','rot_vec1','rot_vec2','rot_vec3','g_vec0','g_vec1','g_vec2','lin_acc0','lin_acc1','lin_acc2'])

df2 = pd.read_csv('21_04_2020_11_42_49_5559.csv')
df3 = df2
df2.drop(df2.columns [[0]], axis=1, inplace=True)
last = df2.time.iat[-1]
print (last)
n = 10


while (n < last):
    s = pd.Series([None,None,None,None,n,None,None,None,None,None,None,None,None,None,None,None],index=['image_name','hand_target_bin','paint_target_bin', 'computer_time', 'time', 'calib_status','rot_vec0','rot_vec1','rot_vec2','rot_vec3','g_vec0','g_vec1','g_vec2','lin_acc0','lin_acc1','lin_acc2'])
    print (s)
    n = n + 10
    df = df.append (s, ignore_index = True)


df2 = df2.append (df, ignore_index = True)
df2 = df2.sort_values(by=['time'])
df = df.loc[:, ['image_name','hand_target_bin','paint_target_bin', 'computer_time', 'time', 'calib_status','rot_vec0','rot_vec1','rot_vec2','rot_vec3','g_vec0','g_vec1','g_vec2','lin_acc0','lin_acc1','lin_acc2']]

df2['image_name'].ffill(inplace=True)
df2['hand_target_bin'].ffill(inplace=True)
df2['paint_target_bin'].ffill(inplace=True)
df2['calib_status'].ffill(inplace=True)

df2['computer_time'] = df2['computer_time'].interpolate (method = 'linear')

df2['g_vec0'] = df2['g_vec0'].interpolate (method = 'linear')
df2['g_vec1'] = df2['g_vec1'].interpolate (method = 'linear')
df2['g_vec2'] = df2['g_vec2'].interpolate (method = 'linear')

df2['lin_acc0'] = df2['lin_acc0'].interpolate (method = 'linear')
df2['lin_acc1'] = df2['lin_acc1'].interpolate (method = 'linear')
df2['lin_acc2'] = df2['lin_acc2'].interpolate (method = 'linear')

df2['rot_vec0'] = df2['rot_vec0'].interpolate (method = 'linear')
df2['rot_vec1'] = df2['rot_vec1'].interpolate (method = 'linear')
df2['rot_vec2'] = df2['rot_vec2'].interpolate (method = 'linear')
df2['rot_vec3'] = df2['rot_vec3'].interpolate (method = 'linear')

df2[['computer_time', 'time','rot_vec0','rot_vec1','rot_vec2','rot_vec3','g_vec0','g_vec1','g_vec2','lin_acc0','lin_acc1','lin_acc2']] = df2[['computer_time', 'time', 'rot_vec0','rot_vec1','rot_vec2','rot_vec3','g_vec0','g_vec1','g_vec2','lin_acc0','lin_acc1','lin_acc2']].astype(float).round(5)

df2 = df2.drop(df2[(df2['time'] % 10) != 0].index)

df2.to_csv('21_04_2020_11_42_49_5559.csv', index=False)
