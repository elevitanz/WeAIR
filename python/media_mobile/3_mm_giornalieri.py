import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings
## file csv giornalieri con le medie mobili
warnings.filterwarnings("ignore")

db_total = pd.read_csv('../tot_media_mobile.csv')
db_total = db_total.drop(columns = ['Unnamed: 0'])
gruppi = db_total.groupby('DATE')
for nome_gruppo, gruppo in gruppi:
    print(nome_gruppo)
    print(gruppo)
    gruppo.to_csv('../'+nome_gruppo[:2]+'_'+nome_gruppo[3:5]+'.csv')