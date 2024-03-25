import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings

warnings.filterwarnings("ignore")

##Plot totali con le medie mobili
db_total = pd.read_csv('../tot_media_mobile.csv')
db_total = db_total.drop(columns = ['Unnamed: 0'])
import pdb; pdb.set_trace()
colonne = ['AMBT', 'AMBH','AMBP', 'CO', 'NO2', 'CO2','MASS_PM10']

max_min_per_colonna = {}
for colonna in colonne:
	db_total[colonna] = pd.to_numeric(db_total[colonna], errors='coerce')
	massimo = db_total[colonna].max()
	minimo = db_total[colonna].min()
	max_min_per_colonna[colonna] = [minimo, massimo]

for colonna in colonne:
	db_total[colonna] = pd.to_numeric(db_total[colonna], errors='coerce')
	minimo = max_min_per_colonna[colonna][0]
	massimo = max_min_per_colonna[colonna][1]
	plt.figure(figsize=(10, 6))
	plt.scatter(db_total.index, db_total[colonna], color='blue', marker='.')
	# plt.title('Graphic '+ colonna)
	plt.xlabel('Date')
	plt.ylabel('Value')
	plt.ylim(minimo - np.abs(minimo/100), massimo + np.abs(massimo/100))
	#plt.grid(True)
	last_date = None
	unique_indices = [0]
	plt.axvline(x=0, color='red', linestyle='--')
	for index in range(1, len(db_total)):
		current_date = db_total.loc[index, 'DATE']
		previous_date = db_total.loc[index - 1, 'DATE']
		if current_date != previous_date:
			unique_indices.append(index)
			plt.axvline(x=index, color='red', linestyle='--')
			#plt.text(index, plt.gca().get_ylim()[1], current_date, rotation=45, ha='right')

	unique_dates = db_total.loc[unique_indices, 'DATE']
	plt.xticks(unique_indices, unique_dates, rotation=90)

	ticks = plt.gca().get_xticks()
	index_3101 = unique_indices[unique_dates.tolist().index('31/01/2024')]
	try:
		index_tick_3101 = np.where(ticks == index_3101)[0][0]
		ticks[index_tick_3101] -= 0.2
	except IndexError:
		pass
	index_0102 = unique_indices[unique_dates.tolist().index('01/02/2024')]
	try:
		index_tick_0102 = np.where(ticks == index_0102)[0][0]
		ticks[index_tick_0102] += 0.2
	except IndexError:
		pass

	plt.gca().set_xticks(ticks)

	plt.tight_layout()
	# plt.show()
	plt.savefig('../mm_tot_plot_'+colonna+'.png', bbox_inches='tight', pad_inches=0.05, dpi=600)
	plt.close()
	print(colonna)