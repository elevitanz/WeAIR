import gpxpy
import pandas as pd
import os

## MERGE FILE LOCALIZZAZIONE e poi giornalieri
df0 = pd.read_csv('../LocalizzazioniTracker/gennaio.csv')
l = ['febbraio_1','febbraio_2']
for val in l:
    df = pd.read_csv('../LocalizzazioniTracker/'+val+'.csv')
    df0 = pd.concat([df0,df], ignore_index=True)
df0 = df0.drop(columns = ['Unnamed: 0','Unnamed: 0.1','Unnamed: 0.2'])
df0['day'] = df0['time'].str[8:10]
for i, elem in df0.iterrows():
	nuovo_valore = elem['time'][:11] + str(int(elem['time'][11:13]) + 1) + elem['time'][13:]
	df0.at[i, 'time'] = nuovo_valore
import pdb; pdb.set_trace()

df0.to_csv('../LocalizzazioniTracker/tot_locat.csv')
gruppi = df0.groupby('day')
for nome_gruppo, gruppo_df in gruppi:
    nome_file = f"{nome_gruppo}.csv"
    gruppo_df.to_csv('../LocalizzazioniTracker/daily/'+nome_file, index=False) 