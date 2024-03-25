import pandas as pd
import numpy as np
### fusione giorni (concatenazione)

l1 = ['22','23','24','25','26','27','28','29', '31'] # 31
l2 = ['01','04','05','07','08','09','10', '12', '13','14','15','16', '18'] # 09,10,15,16
l = l1 + l2
db0 = pd.read_csv('../final/'+l[0]+'.csv')
for i in range(1,len(l)):
	db = pd.read_csv('../final/'+l[i]+'.csv')
	nan_indices = db[db['latitude'].isna()].index
	print(nan_indices)
	db0 = pd.concat([db0, db], axis=0, ignore_index=True)
	db0 = db0.drop(columns = ['Unnamed: 0'])
db0 = db0.drop(columns = ['day'])
for j, el in db0.iterrows():
	print(j, el['CH1'])
import pdb; pdb.set_trace()
db0.to_csv('../superfinal/finale.csv')

