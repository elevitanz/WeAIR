import pandas as pd
import warnings
###SINCRONIZZAZIONE TRA I TEMPI DEI DUE DATAFRAME: SOGLIA DI 5 SECONDI
warnings.filterwarnings("ignore")

def variation(row_1,row_2):
    # Divide gli orari nei rispettivi componenti (ore, minuti, secondi)
    start_hours, start_minutes, start_seconds = map(int, row_1.split(':'))
    end_hours, end_minutes, end_seconds = map(int, row_2.split(':'))
    
    # Calcola la differenza in secondi
    row_1_sec = start_hours * 3600 + start_minutes * 60 + start_seconds
    row_2_sec = end_hours * 3600 + end_minutes * 60 + end_seconds
    diff = abs(row_2_sec - row_1_sec)
    
    return diff

def max_var(df):
	df['variazione'] = 0
	for j in range(len(df)-1):
		df['variazione'].loc[j] = variation(df['TIME'].loc[j+1],df['TIME'].loc[j])
	max_variazione = df['variazione'].max()
	return df['variazione'], max_variazione
# l1 = ['22','23','24','25','26','27','28','29']
l1 = []
l2 = ['14', '18']
# l2 = ['04','05','07','08', '12', '13','14', '18']
l = l1 + l2
for i in l:
    if i == '01' or i == '08': ##caso specifico da event cancellare
        sens = pd.read_csv('../2024_02_'+i+'_LogSeiMon.csv', sep = ';') #2024_02_08_LogSeiMon
        if i == '01':
            sens = sens[:-2]
        locat = pd.read_csv('../LocalizzazioniTracker/daily/'+i+'.csv') #2024-02-08.csv
    elif i in l2:
        sens = pd.read_csv('../2024_02_'+i+'_LogSeiMon.csv') # 2024_02_08_LogSeiMon.csv
        locat = pd.read_csv('../LocalizzazioniTracker/daily/'+i+'.csv') #2024-02-08.csv
        if i == '04' or i == '05':
            sens = sens[:-1]
        if i == '14':
            sens = sens.drop(935)
    elif i in l1:
        sens = pd.read_csv('../2024_01_'+i+'_LogSeiMon.csv')
        locat = pd.read_csv('../LocalizzazioniTracker/daily/'+i+'.csv') #08.csv
    locat['DATE'] = locat['time'].str.slice(stop=10)
    locat['TIME'] = locat['time'].str.slice(start = 11, stop = -6)
    locat['DATE'] = locat['DATE'].str.slice(start=-2)
    locat =locat.drop(columns=['time'])
    if i in l2:
        locat['DATE'] = i + '/02/2024'
    elif i in l1:
        locat['DATE'] = i + '/01/2024'
    locat['TIME_NEW'] = 'TO_DO'
    if i == '26':
        sens = sens.drop(2685)
    y = 5  # Soglia dei secondi
    start_index = 0
    final_index = len(sens)
    for k in range(start_index, final_index):
        print('Riga '+str(k) + 'su '+ str(len(sens)))
        row_df1 = sens.iloc[k]
        time_df1 = row_df1['TIME']

        for j in range(len(locat)):
            row_df2 = locat.iloc[j]
            diff = variation(row_df1['TIME'], row_df2['TIME'])
            row_df2['DIFF'] = diff
            if diff <= y:
                locat.at[j, 'TIME_NEW'] = time_df1
            else:
                pass
    locat['TIME_SENS'] = sens['TIME']
    print(locat['TIME_NEW'])
    print(locat.loc[locat['TIME_NEW'] != 'TO_DO', 'TIME_NEW'])
    print(i)
    import pdb; pdb.set_trace()
    locat.to_csv('../LocalizzazioniTracker_new/'+i+'.csv')



