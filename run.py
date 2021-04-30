import numpy as np
import pandas as pd
import datetime as dt


def slope(x1, y1, x2, y2):
    print(x1)
    print(y1)
    print(x2)
    print(y2)
    return (y2-y1)/(x2-x1)

def calc_returns(data_df):
    nrows = data_df.shape[0]
    yr = data_df.tail(1).index[-1].year
    r7 = ((data_df - data_df.shift(7))/data_df.shift(7)).tail(1)
    r20 = ((data_df - data_df.shift(20))/data_df.shift(20)).tail(1)
    r65 = ((data_df - data_df.shift(65))/data_df.shift(65)).tail(1)
    r120 = ((data_df - data_df.shift(120))/data_df.shift(120)).tail(1)
    r365 = ((data_df - data_df.shift(nrows-1))/data_df.shift(nrows-1)).tail(1)

    returns_df = pd.concat([r7,r20,r65,r120,r365], axis=0, keys=['7','20','65','120','365'])

    print(returns_df)
    print(returns_df.loc['7']['ARKG'][0])
    

def calc_momentum(data_df):
    nrows = data_df.count()
    
    print('\r\n\r\n==========begin calc_momentum=============')
    df_diff = (data_df-data_df.shift(1)).tail(17)
    r4  = pd.DataFrame(data=df_diff.iloc[1:4].sum())
    r5  = pd.DataFrame(data=df_diff.iloc[2:5].sum())
    r6  = pd.DataFrame(data=df_diff.iloc[3:6].sum())
    r7  = pd.DataFrame(data=df_diff.iloc[4:7].sum())
    r8  = pd.DataFrame(data=df_diff.iloc[5:8].sum())
    r9  = pd.DataFrame(data=df_diff.iloc[6:9].sum())
    r10 = pd.DataFrame(data=df_diff.iloc[7:10].sum())
    r11 = pd.DataFrame(data=df_diff.iloc[8:11].sum())
    r12 = pd.DataFrame(data=df_diff.iloc[9:12].sum())
    r13 = pd.DataFrame(data=df_diff.iloc[10:13].sum())
    r14 = pd.DataFrame(data=df_diff.iloc[11:14].sum())
    r15 = pd.DataFrame(data=df_diff.iloc[12:15].sum())
    r16 = pd.DataFrame(data=df_diff.iloc[13:16].sum())
    r17 = pd.DataFrame(data=df_diff.iloc[14:17].sum())
    

    frames = [r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17]
    all_frames = pd.concat(frames, axis=1, ignore_index=True).transpose()

    result = pd.DataFrame()
    asum = all_frames.iloc[7:14].sum()
    prev_sum = all_frames.iloc[0:7].sum()
    result['sum'] = asum
    result['prev_sum'] = prev_sum
    print(result)
    print('\r\n\r\n==========end calc_momentum=============')

if __name__ == '__main__':
    d_parser = lambda x: pd.to_datetime(x)
    data_df = pd.read_csv('data.csv', parse_dates=['Date'], date_parser=d_parser, index_col='Date')
    #print(data_df.head())
    #print(data_df.tail())
    #print(data_df) # get 11 cols of first row
    #print(data_df.iloc[252,1:11]) # get 11 cols of last row
    #print((data_df / data_df.iloc[252,1:11])) # calc return for each col
    #calc_returns((data_df))
    calc_momentum(data_df)
