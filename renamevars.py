import pandas as pd
def renamevars(df, dict_names):
    return df.rename(columns=dict_names, inplace=False) 
    return renamed_df