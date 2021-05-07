import numpy as np
import pandas as pd
import datetime as dt
import utils

def find_first_trading_year_of_day(yr: int, df: pd.DataFrame):
    i=0
    for idx in df.index:
        if pd.to_datetime(idx).year == yr:
            break
        i += 1
    return i

def calc_returns(data_df):
    nrows = data_df.shape[0]
    yr = data_df.index[nrows-1].year
    i = find_first_trading_year_of_day(yr, data_df)-1
    r7 = ((data_df - data_df.shift(7))/data_df.shift(7)).tail(1)
    r20 = ((data_df - data_df.shift(20))/data_df.shift(20)).tail(1)
    r65 = ((data_df - data_df.shift(65))/data_df.shift(65)).tail(1)
    r120 = ((data_df - data_df.shift(120))/data_df.shift(120)).tail(1)
    r365 = ((data_df - data_df.shift(nrows-1))/data_df.shift(nrows-1)).tail(1)
    rytd = ((data_df - data_df.shift(nrows-i-1))/data_df.shift(nrows-i-1)).tail(1)

    wts_idx = pd.Series(['7','20','65','120','365','ytd'], name='wts')
    returns_df = pd.concat([r7,r20,r65,r120,r365,rytd], axis=0, keys=wts_idx, ignore_index=True)
    #returns_df = pd.concat([r7,r20,r65,r120,r365,rytd], axis=0)

    #print(returns_df)
    # print(returns_df.loc['7']['ARKG'][0])

    return returns_df
    
def calc_wtd_return(data_df):
    
    s0 = data_df.iloc[0] * utils.Constants.returns_weights.loc['7']
    s1 = data_df.iloc[1] * utils.Constants.returns_weights.loc['20']
    s2 = data_df.iloc[2] * utils.Constants.returns_weights.loc['65']
    s3 = data_df.iloc[3] * utils.Constants.returns_weights.loc['120']
    s5 = data_df.iloc[5] * utils.Constants.returns_weights.loc['ytd']
    result = pd.concat([s0,s1,s2,s3,s5], axis=1)
    #print(result)
    #print(result.sum(axis=1))
    return(result)


def calc_momentum(data_df):
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
    #print(result)
    #utils.print_df(result)
    return result
   
    print('\r\n\r\n==========end calc_momentum=============')

def calc_allocations(wtd_returns):
    tot = wtd_returns.loc['SPY'].sum() + wtd_returns.loc['QQQ'].sum() + wtd_returns.loc['IJH'].sum()+ wtd_returns.loc['IJR'].sum() + wtd_returns.loc['VUG'].sum() + wtd_returns.loc['VTV'].sum()
    print(tot)
    print("Allocation for SPY {:2.2f}%".format(wtd_returns.loc['SPY'].sum() / tot * 100))
    print("Allocation for QQQ {:2.2f}%".format(wtd_returns.loc['QQQ'].sum() / tot * 100))

if __name__ == '__main__':
    d_parser = lambda x: pd.to_datetime(x)
    data_df = pd.read_csv('data.csv', parse_dates=['Date'], date_parser=d_parser, index_col='Date')
    #data_df = pd.read_csv('data.csv')
    #utils.print_df(data_df.head())
    print(data_df.tail())
    #print(data_df) # get 11 cols of first row
    #print(data_df.iloc[252,1:11]) # get 11 cols of last row
    #print((data_df / data_df.iloc[252,1:11])) # calc return for each col
    momentum = calc_momentum(data_df)
    returns = calc_returns(data_df)
    print(momentum)
    print(returns)
    wtd_returns = calc_wtd_return(returns)
    print(wtd_returns)
    print(wtd_returns.sum(axis=1))

    calc_allocations(wtd_returns)
    # print(returns)
    # result = returns.mul(utils.Constants.returns_weights, axis=0)
    # utils.print_df(result)
    print('done')