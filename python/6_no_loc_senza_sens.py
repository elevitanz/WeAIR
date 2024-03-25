import pandas as pd
import numpy as np
### cancellare i casi in cui hai localizzazioni ma non dati sensore

l1 = ['22','23','24','25','26','27','28','29']
l2 = ['01','04','05','07','08', '12', '13','14', '18']
l = l1 + l2
for i in l:
	db = pd.read_csv('../dati_metro_giornalieri_intersezione/'+i+'_merged_sorted.csv')
	db = db.drop(columns = ['Unnamed: 0', 'Unnamed: 0.1'])
	rows_to_drop = []
	for j in range(len(db)):
		if not pd.isnull(db.iloc[j]['latitude']) and pd.isnull(db.iloc[j]['NUM_PM10']):
		# if not np.isnan(db.iloc[j]['latitude']) and np.isnan(db.iloc[j]['NUM_PM10']):
			rows_to_drop.append(j)
	print(rows_to_drop)
	if len(rows_to_drop) != 0:
		db = db.drop(rows_to_drop)
		db.reset_index(drop=True, inplace=True)
		db.to_csv('../dati_metro_giornalieri_intersezione/'+i+'_merged_sorted_fixed.csv')
	else:
		db.to_csv('../dati_metro_giornalieri_intersezione/'+i+'_merged_sorted_fixed.csv')
import pdb; pdb.set_trace()