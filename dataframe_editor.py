import pandas as pd

aux = df.name.str.split('_',expand=True)
aux.columns = ['phon','R','subject_id','trial']
df['subject_id'] = aux.subject_id
df['trial'] = aux.trial
df.drop(df.columns[[0]], axis=1, inplace=True)
new_df=df
