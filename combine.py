import pandas as pd
import glob
import sh

df_csv_append = pd.DataFrame()
csv_files = glob.glob('21*.{}'.format('csv'))

# append the CSV files
for file in csv_files:
    df1 = pd.read_csv ('11_42_49_0.csv', index_col=False)
    df = pd.read_csv(file,index_col=False)
    df.drop('#id', axis=1, inplace=True)
    df1.drop('#id', axis=1, inplace=True)
    length = len(df)
    df1 = df1.sort_index()
    df1.truncate(after=length)
    df1.reset_index(drop=True, inplace=True)
    df.reset_index(drop=True, inplace=True)
    df_merged = pd.concat ([df1[:length], df], axis=1)
    df_merged.to_csv(file)
    
for file in csv_files:
    first = "#id,image_name,hand_target_bin,paint_target_bin,computer_time, time, calib_status, rot_vec0, rot_vec1, rot_vec2, rot_vec3, g_vec0, g_vec1, g_vec2, lin_acc0, lin_acc1, lin_acc2"
    sh.sed("-i", "1s/.*/" + first + "/", file)

