def renamevars(df, dict_names):
    renamed_df = df.copy()
    renamed_df.columns = [dict_names[col] if col in dict_names else col for col in df.columns] 
    return renamed_df