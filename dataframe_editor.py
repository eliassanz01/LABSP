import pandas as pd

df=pd.read_csv(dataframe)
aux = df.name.str.split('_',expand=True)
aux.columns = ['phon','R','subject_id','trial']
df['subject_id'] = aux.subject_id
df['trial'] = aux.trial
df_new=df.drop(['name'], axis=1)
