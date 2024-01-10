def normalize(df,op):
    if op == 0:
        numeric_vals = df._get_numeric_data()
        norm_df=(numeric_vals-numeric_vals.mean())/numeric_vals.std()
    else:
        numeric_vals = df._get_numeric_data()
        norm_df=(numeric_vals - numeric_vals.min()) / (numeric_vals.max() - numeric_vals.min())
    return norm_df
