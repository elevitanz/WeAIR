import pandas as pd

### ordinare secondo i tempi

l1 = ['22','23','24','25','26','27','28','29']
l2 = ['01','04','05','07','08', '12', '13','14', '18']
l = l1 + l2
def converti_orario(orario):
    ore, minuti, secondi = orario.split(':')
    return f"{int(ore):02d}{int(minuti):02d}{int(secondi):02d}"

for i in l:
	db = pd.read_csv('../dati_metro_giornalieri_intersezione/'+i+'_merged.csv')
	db.dropna(subset=['TIME'], inplace=True)
	db = db[db['TIME'].str.match(r'^\d{2}:\d{2}:\d{2}$')]
	db.reset_index(drop=True, inplace=True)
	db_sorted = db.iloc[db['TIME'].apply(converti_orario).argsort()]
	db_sorted.reset_index(drop=True, inplace=True)
	db_sorted = db_sorted.drop(columns = ['Unnamed: 0', 'DATE','DATE1','TIME_OLD'])
	if i in l1:
		db_sorted['DATE'] = i+'/01/2024'
	elif i in l2:
		db_sorted['DATE'] = i+'/02/2024'
	db_sorted.to_csv('../dati_metro_giornalieri_intersezione/'+i+'_merged_sorted.csv')
	print(i)