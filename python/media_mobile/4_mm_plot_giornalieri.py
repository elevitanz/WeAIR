import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings

warnings.filterwarnings("ignore")

##Plot giornalieri con le medie mobili
db_total = pd.read_csv('../tot_media_mobile.csv')
db_total = db_total.drop(columns = ['Unnamed: 0'])
colonne = ['AMBT', 'AMBH','AMBP', 'CO', 'NO2', 'CO2','MASS_PM10']
#colonne = ['CO', 'CO2','NO2']
max_min_per_colonna = {}
for colonna in colonne:
	db_total[colonna] = pd.to_numeric(db_total[colonna], errors='coerce')
	massimo = db_total[colonna].max()
	minimo = db_total[colonna].min()
	max_min_per_colonna[colonna] = [minimo, massimo]

#l1 = ['22','23','24','25','26','27','28','29', '31'] # 31
#l2 = ['01','04','05','07','08','09','10', '12', '13','14','15','16', '18']
l2 = ['10', '12', '13','14','15','16', '18'] # 09,10,15,16
l1 = []
# l2 = []
l = l1 + l2
for i in range(len(l1)):
	print(l1[i])
	db = pd.read_csv('../'+l1[i]+'_01.csv')
	db = db.drop(columns = ['Unnamed: 0'])
	for colonna in colonne:
		db[colonna] = pd.to_numeric(db[colonna], errors='coerce')
		minimo = max_min_per_colonna[colonna][0]
		massimo = max_min_per_colonna[colonna][1]
		plt.figure(figsize=(10, 6))
		plt.scatter(db['TIME'], db[colonna], color='blue', marker='.')
		plt.title('Graphic '+ l1[i] +' 01 '+ colonna)
		plt.xlabel('Date')
		plt.ylabel('Value')
		plt.ylim(minimo - np.abs(minimo/100), massimo + np.abs(massimo/100))
		#plt.grid(True)
		plt.xticks(rotation=45)
		ticks = plt.gca().get_xticks()
		plt.xticks([ticks[0], ticks[-1]])
		plt.tight_layout()
		#plt.show()
		plt.savefig('../plot_'+ l1[i] +'_01_'+colonna+'.png', bbox_inches='tight', pad_inches=0.05, dpi=600)
		plt.close()
		plt.clf()
		print(colonna)
for i in range(len(l2)):
	db = pd.read_csv('../'+l2[i]+'_02.csv')
	db = db.drop(columns = ['Unnamed: 0'])
		# db['MASS_PM4.0'] = pd.to_numeric(db['MASS_PM4.0'], errors='coerce')
		# non_numeric_values = db.loc[db['MASS_PM4.0'].isna(), 'MASS_PM4.0']
		# print("Valori non numerici nella colonna 'MASS_PM4.0':")
		# print(non_numeric_values)
	for colonna in colonne:
		db[colonna] = pd.to_numeric(db[colonna], errors='coerce')
		minimo = max_min_per_colonna[colonna][0]
		massimo = max_min_per_colonna[colonna][1]
		plt.figure(figsize=(10, 6))
		plt.scatter(db['TIME'], db[colonna], color='blue', marker='.')
		plt.title('Graphic '+ l2[i] +' 02 '+ colonna)
		plt.xlabel('Date')
		plt.ylabel('Value')
		plt.ylim(minimo - np.abs(minimo/100), massimo + np.abs(massimo/100))
		#plt.grid(True)
		plt.xticks(rotation=45)
		ticks = plt.gca().get_xticks()
		plt.xticks([ticks[0], ticks[-1]])
		plt.tight_layout()
		plt.savefig('../plot_'+ l2[i] +'_02_'+colonna+'.png', bbox_inches='tight', pad_inches=0.05, dpi=600)
		plt.close()
		plt.clf()
		print(colonna)



