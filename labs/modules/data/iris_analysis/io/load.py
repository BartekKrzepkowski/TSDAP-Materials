import pandas as pd

def load_df(path):
    df = pd.read_csv(path).iloc[:, :4]
    return df