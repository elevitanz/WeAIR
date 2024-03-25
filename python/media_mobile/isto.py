import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings
## istogramma con occorrenze orarie
warnings.filterwarnings("ignore")

db_total = pd.read_csv('../tot_media_mobile.csv')
db_total = db_total.drop(columns = ['Unnamed: 0'])
db_total['HOUR'] = db_total['TIME'].str[:2]
db_total['DAY'] = db_total['DATE'].str[:2]
gruppi = db_total.groupby('DAY')
hours = {}
for nome_gruppo, gruppo in gruppi:
    hours[nome_gruppo] = sorted(set(gruppo['HOUR']))

lis =['00','01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12',
'13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
occorrenze_ore = {hour: 0 for hour in lis}
for ore in hours.values():
	for ora in ore:
		occorrenze_ore[ora] += 1

import pdb; pdb.set_trace()
ore = list(occorrenze_ore.keys())
occorrenze = list(occorrenze_ore.values())

plt.bar(ore, occorrenze, align='center', alpha=0.5)
plt.xlabel('Hours')
plt.ylabel('Occurrences')
plt.title('')
plt.xticks(lis)
plt.yticks(range(0, max(occorrenze)+1, 1))
plt.grid(True)

plt.savefig('../occurrences.png', dpi= 600)
