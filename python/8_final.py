import pandas as pd
import numpy as np
### Sincronizzazione delle localizzazioni mancanti tra giorni diversi + gestione primi e ultimi giorni

l1 = ['22','23','24','25','26','27','28','29', '31'] # 31
l2 = ['01','04','05','07','08','09','10', '12', '13','14','15','16', '18'] # 09,10,15,16
l = l1 + l2
for i in range(len(l)):
	if l[i] != '09' and l[i] != '15':
		db = pd.read_csv('../final/'+l[i]+'.csv')
	elif l[i] == '09' or l[i] == '15':
		db = pd.read_csv('../final/'+l[i]+'.csv', delimiter=';')
		db.rename(columns={',DATE': 'DATE'}, inplace=True)
		db['DATE'] = db['DATE'].str[-10:]
	if 'Unnamed: 0' in db.columns:
		db = db.drop(columns = ['Unnamed: 0'])
	if i == 0:
		for j, el in db.iterrows():
			if not np.isnan(el['latitude']):
				lat = el['latitude']
				lon = el['longitude']
				elev = el['elevation']
				break
		db['latitude'].fillna(lat, inplace=True)
		db['longitude'].fillna(lon, inplace=True)
		db['elevation'].fillna(elev, inplace=True)

	if l[i] == '31':
		db['latitude'] = None ##VEDI ULTIMO DEL 29
		db['longitude'] = None
		db['elevation'] = None
		db['day'] = db['DATE'].str[:2]

	if l[i] == '09' or l[i] == '10': ##VEDI ULTIMO DELL'8
		db['latitude'] = None
		db['longitude'] = None
		db['elevation'] = None
		db ['day'] = db['DATE'].str[:2]
	if l[i] == '15' or l[i] == '16': ##VEDI ULTIMO DEL 14
		db['latitude'] = None
		db['longitude'] = None
		db['elevation'] = None
		db['day'] = db['DATE'].str[:2]
	nan_indices = db[db['latitude'].isna()].index
	if i != 0 and not nan_indices.empty:
		db_rif = pd.read_csv('../final/'+l[i-1]+'.csv')
		new_lat = db_rif['latitude'].iloc[-1]
		new_long = db_rif['longitude'].iloc[-1]
		new_elev = db_rif['elevation'].iloc[-1]
		for ind in nan_indices:
			db.loc[ind, 'latitude'] = new_lat
			db.loc[ind, 'longitude'] = new_long
			db.loc[ind, 'elevation'] = new_elev
	import pdb; pdb.set_trace()
	db.to_csv('../final/'+l[i]+'.csv')
	# print('NAN \n',nan_indices)
	# print('DB \n',db)
	# print('COLUMNS \n',db.columns)