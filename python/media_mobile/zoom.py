import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings

warnings.filterwarnings("ignore")

##Plot giornalieri con le medie mobili
db_total = pd.read_csv('../tot_media_mobile.csv')
db_total = db_total.drop(columns = ['Unnamed: 0'])
#colonne = ['AMBT', 'AMBH','AMBP', 'CO', 'NO2', 'CO2','MASS_PM10']
colonne = ['CO']
max_min_per_colonna = {}

#l1 = ['22','23','24','25','26','27','28','29', '31'] # 31
#l2 = ['01','04','05','07','08','09','10', '12', '13','14','15','16', '18']
l2 = ['18']
# db2 = pd.read_csv('../../../dati_fissi_QA/dati_orari_2701_26_02.csv')
# db_temp = pd.read_csv('../../../dati_fissi_QA/temp_15min_24.csv', delimiter=';')
# db_temp['valore'] = db_temp['valore'].str.replace(',', '.')
# db_temp['DATE'] = db_temp['yyyy-mm-dd hh:mm'].str.slice(0, 10)
# db_temp['HOUR'] = db_temp['yyyy-mm-dd hh:mm'].str.slice(11,17)
# db_temp = db_temp[2016:4608]
# db_temp = db_temp[db_temp['DATE'] == '18-02-2024']
# db_temp = db_temp.reset_index()
# db_temp['valore'] = pd.to_numeric(db_temp['valore'], errors='coerce')
# colonne_db2 = ['COmedia oraria (µg/m≥)', 'NO2media oraria (µg/m≥)']
# colonne_db2 = ['NO2media oraria (µg/m≥)']
# db2['DATE'] = db2['Data Ora Osservazione'].str.slice(0, 10)
# db2['HOUR'] = db2['Data Ora Osservazione'].str.slice(11,14)
# db2 = db2[db2['DATE'] == '18-02-2024']
# for colonna_db2 in colonne_db2:
# 	for index, row in db2.iterrows():
# 		if '-' in row[colonna_db2]:
# 			db2.drop(index, inplace=True)
# db2 = db2.reset_index()
# db2 = db2.drop(columns = ['index', 'Data Ora Osservazione', 'PM10media oraria (µg/m≥)'])
for i in range(len(l2)):
	db = pd.read_csv('../'+l2[i]+'_02.csv')
	db = db.drop(columns = ['Unnamed: 0'])
	for colonna in colonne:
		db[colonna] = pd.to_numeric(db[colonna], errors='coerce')
		plt.figure(figsize=(10, 6))
		if 'CO' in colonna:
			plt.scatter(db['TIME'][:210], db[colonna][:210], color='blue', marker='.')
		elif 'NO2' in colonna:
			import pdb; pdb.set_trace()
			db[colonna] = db[colonna] - 0.5
			plt.scatter(db['TIME'], db[colonna], color='blue', marker='.')
		if 'NO2' in colonna:
			v = round(0.029772, 2)
			plt.axhline(y=v, color='r', linestyle='-')
			# plt.title(l2[i] +' 02 - NO2')
		elif 'CO' in colonna:
			v = round(0.436, 2)
			plt.axhline(y=v, color='r', linestyle='-')
			# plt.title(l2[i] +' 02 - CO')
			plt.ylim(0, 0.8)
		plt.xlabel('Time')
		plt.ylabel('Value')
		#plt.grid(True)
		plt.xticks(rotation=45)
		ticks = plt.gca().get_xticks()
		plt.xticks([ticks[0], ticks[-1]])
		plt.tight_layout()
		#plt.show()
		plt.savefig('../new_zoom_plot_'+ l2[i] +'_02_'+colonna+'.png', bbox_inches='tight', pad_inches=0.05, dpi=600)
		plt.close()
		plt.clf()
		print(colonna)



