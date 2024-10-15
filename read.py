import sh
import glob
import pandas as pd

df_csv_append = pd.DataFrame()
csv_files = glob.glob('21*.{}'.format('csv'))
count = 0

for file in csv_files:
    
    df = pd.read_csv(file)
    print (">>>", file)
    print ()
    print ("lines: ", len(df))
    x = len(df)
    print("ct_beg: ", df['computer_time'].iat[0])
    print("ct_end: ", df['computer_time'].iat[(x-1)])
    print("ct_delta: ", ((df['computer_time'].iat[(x-1)]) - (df['computer_time'].iat[0])))
    ct_delta = ((df['computer_time'].iat[(x-1)]) - (df['computer_time'].iat[0]))
    print("t_beg: ", df['time'].iat[0])
    print("t_end: ", df['time'].iat[(x-1)])
    print("------")
    times = []
    times.append (ct_delta)

for z in range (0, len (times)):
    compare = times[0]
    if times[z] < compare:
        compare = times [z]
    print ("Smallest delta: ", compare)
    print ("New lines:", round((compare * 100)))
