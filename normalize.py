def normalize(df,op):
    numeric_vals = df._get_numeric_data()
    if op == 0:
        norm_df=(numeric_vals-numeric_vals.mean())/numeric_vals.std()
    else:
        norm_df=(numeric_vals - numeric_vals.min()) / (numeric_vals.max() - numeric_vals.min())
    return norm_df
