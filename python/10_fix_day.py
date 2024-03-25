import pandas as pd
import numpy as np
### fix day

l1 = ['22','23','24','25','26','27','28','29']
l2 = ['01','04','05','07','08', '12', '13','14', '18']
l = l1 + l2
for i in range(len(l)):
	db = pd.read_csv('../final/'+l[i]+'.csv')
	db = db.drop(columns = ['day', 'Unnamed: 0'])
	db.to_csv('../final/'+l[i]+'.csv')