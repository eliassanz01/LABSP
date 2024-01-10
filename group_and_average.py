def group_and_average(df, gv):
    av_df = df.groupby(gv).mean()
    return av_df