import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings

warnings.filterwarnings("ignore")

## Media mobile su tutto il dataset
db_total = pd.read_csv('../../superfinal/finale.csv')
db_total = db_total.drop(columns = ['Unnamed: 0'])
db_total['MASS_PM2.5'].loc[105548] = 9.4
db_total.rename(columns={'CH0': 'CO', 'CH1': 'NO2'}, inplace=True)
db_total['CO'] = db_total['CO'] + 0.9
db_total['CO2'] = pd.to_numeric(db_total['CO2'], errors='coerce')
db_total.dropna(subset=['CO2'], inplace=True)
db_total['CO2'] = db_total['CO2'].astype(float) + 0.04
colonne = ['AMBT', 'AMBH','AMBP', 'CO', 'NO2', 'CO2', 'CO2_T', 'MASS_PM10']
df_medie_mobili = pd.DataFrame()
for colonna in colonne:
	db_total[colonna] = pd.to_numeric(db_total[colonna], errors='coerce')
	df_medie_mobili[colonna] = db_total[colonna].rolling(window=10, min_periods=1).mean()
	df_medie_mobili = df_medie_mobili.round(2)

colonne_non_specificate = ['DATE','TIME','latitude', 'longitude', 'elevation']
for colonna in colonne_non_specificate:
    df_medie_mobili[colonna] = db_total[colonna]

df_medie_mobili.reset_index(inplace = True, drop = True)
print(df_medie_mobili)
import pdb; pdb.set_trace()
df_medie_mobili.to_csv('../tot_media_mobile.csv')