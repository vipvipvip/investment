import pandas as pd

def print_df(result_df):
    for idx in result_df.index:
        for col in result_df.columns:
            print("Index=%s, Column=%s, Value=%d" % (idx, col, result_df[col].loc[idx]))

def print_series(result_series):
    print([index for index in result_series.values])

class Constants(object):
    wts = pd.Index([.03, .26, .13, .06,.52], name='wts')
    returns_weights = pd.Series(data=wts, index=['ytd', '20', '65', '120', '7'])
    print_series(returns_weights)
    print(returns_weights['ytd'])