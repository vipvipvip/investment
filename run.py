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
    #print(data_df.iloc[[0]])
    #print(data_df.iloc[1:2].index[0])

    print('\r\n****************************')
    print(data_df.diff().tail(1).iloc[0]+data_df.iloc[0:-1].diff().tail(1).iloc[0]+data_df.iloc[0:-2].diff().tail(1).iloc[0])
    #print(data_df.iloc[0:-1].diff().tail(1))
    #print(data_df.iloc[0:-2].diff().tail(1))
    
    #print(data_df.iloc[0])
    #print(data_df.iloc[1])
    #s = slope(data_df.iloc[0:1].index[0],data_df.iloc[0:1],data_df.iloc[1:2].index[0], data_df.iloc[1:2] )
    #print (s)
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
