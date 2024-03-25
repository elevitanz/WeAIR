import pandas as pd
# merge tra dati sensore e dati localizzazione

l1 = ['22','23','24','25','26','27','28','29'] #31
l2 = ['01','04','05','07','08', '12', '13','14', '18'] #09,10,15,16
l = l1 + l2
for i in l:
	if i == '01' or i == '08':
		sens = pd.read_csv('../2024_02_'+i+'_LogSeiMon.csv', sep = ';')
	elif i in l2:
		sens = pd.read_csv('../2024_02_'+i+'_LogSeiMon.csv') # 2024_02_08_LogSeiMon.csv
	elif i in l1:
		sens = pd.read_csv('../2024_01_'+i+'_LogSeiMon.csv')
	locat = pd.read_csv('../LocalizzazioniTracker_new/'+i+'.csv')
	locat = locat.drop(columns = ['Unnamed: 0', 'TIME_SENS'])
	locat['TIME_OLD'] = locat['TIME']
	locat['TIME'] = locat['TIME_NEW']
	locat = locat.drop(columns = ['TIME_NEW'])
	merged_df = pd.merge(locat, sens, on='TIME', how='outer', suffixes=[None,'1'])
	print(i)
	print(len(merged_df))
	print(merged_df)
	print(sens)
	print(locat)
	import pdb; pdb.set_trace()
	merged_df.to_csv('../dati_metro_giornalieri_intersezione/'+i+'_merged.csv')