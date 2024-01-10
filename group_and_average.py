def group_and_average(df, gv):
    numeric_cols = df.select_dtypes(include='number').columns
    result_df = df.groupby(gv)[numeric_cols].mean().reset_index()
    return result_df