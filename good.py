import sh
import glob
import pandas as pd
from scipy.interpolate import interp1d
import numpy as np

df_csv_append = pd.DataFrame()
csv_files = glob.glob('21*.{}'.format('csv'))

start_line_num = 0
end_line_num = 29998

first_line = [0] * 14
upper_line = [0] * 14
interpolated_line = [0] * 14
lower_line = [0] * 14
last_line = [0] * 14
list_of_lists = [0] * 14

first_point = [0] * 2
second_point = [0] * 2

times = [0] * end_line_num
iden = [0] * end_line_num
for i in range (start_line_num, (end_line_num-1)):
    times[i] = i*10
    iden[i] = i

for file in csv_files:    
    df = pd.read_csv(file)
    df2 = df
    df2.drop(['#id', 'computer_time', 'time'], axis=1, inplace=True)
    first_line = df2.loc[start_line_num, :].values.flatten().tolist()
    last_line = df2.loc[(end_line_num-1), :].values.flatten().tolist()
    list_of_lists[0] = first_line

    for i in range (1, end_line_num-2):
        if (((df['time'].iat[i]) <= times[i]) & ((df['time'].iat[(i+1)]) >= times[i])):
            upper_line = df2.loc[i, :].values.flatten().tolist()    
            lower_line = df2.loc[(i+1), :].values.flatten().tolist()
            happening = 1

        elif (((df['time'].iat[i]) <= times[i]) & ((df['time'].iat[(i+2)]) >= times[i])):
            upper_line = df2.loc[i, :].values.flatten().tolist()    
            lower_line = df2.loc[(i+2), :].values.flatten().tolist()
            happening = 2        

        if happening == 1:
            for ii in range (0, 3):
                interpolated_line[ii] = upper_line[ii]

            for ii in range (4, 13): 
                first_point = [df['time'].iat[i], upper_line[ii]]
                second_point = [df['time'].iat[(i+1)], lower_line[ii]]
                print (first_point, "-----", second_point, "-----", times[i])
                ifunc = interp1d (first_point, second_point)
                new_point = ifunc (times[i])
        if happening == 2:
 
            for ii in range (0, 3):
                interpolated_line[ii] = upper_line[ii]

            for ii in range (4, 13): 
                first_point = [df['time'].iat[i], upper_line[ii]]
                second_point = [df['time'].iat[(i+2)], lower_line[ii]]
                ifunc = interp1d (first_point, second_point)
                new_point = ifunc (times[i])

        interpolated_line.append (new_point)
                        

        list_of_lists.append (interpolated_line)
 
    list_of_lists.append (last_line)
    df_new = pd.DataFrame(list_of_lists, columns = ['image_name','hand_target_bin','paint_target_bin','calib_status','rot_vec0','rot_vec1','rot_vec2','rot_vec3','g_vec0','g_vec1','g_vec2','lin_acc0','lin_acc1','lin_acc2'])
    df_new.insert(0, "#id", iden)
    df_new.insert(4, "time", times)
    df_new.to_csv("new_",file)


