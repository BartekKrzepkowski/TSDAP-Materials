import pandas as pd

def calc_mean(df):
    return df.mean(axis=0)

def calc_median(df):
    return df.median(axis=0)

def calc_std(df):
    return df.std(axis=0)

def calc(df):
    mean = calc_mean(df)
    median = calc_median(df)
    std = calc_std(df)
    df_results = pd.concat([mean, median, std], axis=1)
    df_results.columns = ['mean', 'median', 'std']
    return df_results