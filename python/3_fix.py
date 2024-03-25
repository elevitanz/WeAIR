import pandas as pd

### TOGLIE I TO_DO NELLA COLONNA TIME DELLE LOCALIZZAZIONI

l1 = ['22','23','24','25','26','27','28','29']
l2 = ['01','04','05','07','08', '12', '13','14', '18']
l = l1 + l2
for i in l:
	prova = pd.read_csv('../LocalizzazioniTracker_new/'+i+'.csv')
	for k in range(len(prova)):
		if prova['TIME_NEW'].loc[k] == 'TO_DO':
			prova['TIME_NEW'].loc[k] = prova['TIME'].loc[k]
	prova.to_csv('../LocalizzazioniTracker_new/'+i+'.csv')
import pdb; pdb.set_trace()