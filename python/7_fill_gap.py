import pandas as pd
import numpy as np
### sincronizzazione delle localizzazioni mancanti intra stessi giorni

l1 = ['22','23','24','25','26','27','28','29']
l2 = ['01','04','05','07','08', '12', '13','14', '18']
l = l1 + l2
def split_indices(indices):
    split_indices_list = []
    current_split = [indices[0]]
    for i in range(1, len(indices)):
        if indices[i] != indices[i-1] + 1:
            split_indices_list.append(current_split)
            current_split = []
        current_split.append(indices[i])
    split_indices_list.append(current_split)
    return split_indices_list
for i in l:
	db = pd.read_csv('../dati_metro_giornalieri_intersezione/'+i+'_merged_sorted_fixed.csv')
	db = db.drop(columns = ['Unnamed: 0'])
	non_nan_indices = db[db['latitude'].notna()].index
	print(db,'PRIMA')
	if len(non_nan_indices) == 0:
		print(i)
		pass
	else:
		lista_splittata = split_indices(non_nan_indices)
		estremi_inf = []
		estremi_sup = [0]
		for k in range(len(lista_splittata)):
			estremi_inf.append(lista_splittata[k][0] - 1)
			estremi_sup.append(lista_splittata[k][-1] + 1)
		estremi_inf.append(len(db))
		gruppetti = []	
		for g in range(len(lista_splittata)+1):
			gruppetto = []
			for elem in range(estremi_sup[g],estremi_inf[g]+1):
				gruppetto.append(elem)
			gruppetti.append(gruppetto)
		#print(gruppetti)
		for q in range(len(gruppetti)):
			if q == 0:
				pass
			else:
				sample_ind = gruppetti[q][0] - 1
				for ind in gruppetti[q]:
					lat = db.loc[sample_ind]['latitude']
					lon = db.loc[sample_ind]['longitude']
					elev = db.loc[sample_ind]['elevation']
					db.loc[ind, 'latitude'] = lat
					db.loc[ind, 'longitude'] = lon
					db.loc[ind, 'elevation'] = elev
		db.drop(db.index[-1], inplace=True)
	print(db, 'DOPO')
	db.to_csv('../final/'+i+'.csv')