import pandas as pd

def print_df(result_df):
    for idx in result_df.index:
        for col in result_df.columns:
            print("Index=%s, Column=%s, Value=%d" % (idx, col, result_df[col].loc[idx]))

def print_series(result_series):
    print([index for index in result_series.values])

class Constants(object):
    wts = {'ytd': .03, '4weeks': .26, '13weeks': .13, '6months': .06, '1week': .52}
    returns_weights = pd.Series(data=wts, index=['ytd', '4weeks', '13weeks', '6months', '1week'])
    print_series(returns_weights)
    print(returns_weights['ytd'])