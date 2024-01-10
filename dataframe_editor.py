import pandas as pd

def dataframe_editor(dataframe):
    aux = dataframe.name.str.split('_',expand=True)
    aux.columns = ['phon','R','subject_id','trial']
    dataframe['subject_id'] = aux.subject_id
    dataframe['trial'] = aux.trial
    dataframe.drop(dataframe.columns[[0]], axis=1, inplace=True)
    return dataframe
