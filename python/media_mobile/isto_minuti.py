import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings
## istogramma con occorrenze orarie
warnings.filterwarnings("ignore")

db_total = pd.read_csv('../tot_media_mobile.csv')
db_total = db_total.drop(columns = ['Unnamed: 0'])
# db_total = pd.read_csv('../22_01.csv')
# db_total = db_total.drop(columns = ['Unnamed: 0'])
# db_total = db_total[28027:]
# db_total.reset_index(inplace=True,drop=True)
# db_total.to_csv('../22_01.csv')
import pdb; pdb.set_trace()
db_total['HOUR'] = db_total['TIME'].str[:2]
db_total['DAY'] = db_total['DATE'].str[:2]
db_total['MINUTE'] = db_total['TIME'].str[3:5]
gruppi = db_total.groupby('DAY')
minutes = {}
for nome_gruppo, gruppo in gruppi:
	gruppo = gruppo[gruppo['HOUR'] == '19']
	minutes[nome_gruppo] = sorted(set(gruppo['MINUTE']))

lis =['00','01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12',
'13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23','24', '25', '26', '27',
'28','29','30','31','32','33','34','35','36','37','38','39','40','41','42',
'43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59']
occorrenze_minuti = {minute: 0 for minute in lis}
for mins in minutes.values():
	for minu in mins:
		occorrenze_minuti[minu] += 1

mins = list(occorrenze_minuti.keys())
occorrenze = list(occorrenze_minuti.values())

plt.bar(mins, occorrenze, align='center', alpha=0.5)
plt.xlabel('Hours')
plt.ylabel('Occurrences')
plt.title('')
plt.xticks(lis)
plt.yticks(range(0, max(occorrenze)+1, 1))
plt.grid(True)
#plt.show()
plt.savefig('../minutes_occurrences.png', dpi= 600)
