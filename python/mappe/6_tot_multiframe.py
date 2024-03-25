import numpy as np
import osmnx as ox
import pandas as pd
import networkx as nx
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from collections import OrderedDict

### DA RETE A HEATMAP-MULTIFRAME: PLOT TOTALE PER INDICATORE (DA FARE UNA COLONNA PER VOLTA)
monte = (43.321227, 11.330898)
radius = 5000
### CREI UNA COLORMAP TRA min e max PER OGNI COLONNA.
colonne = ['NO2']
#colonne = ['AMBT', 'AMBH','AMBP', 'CO', 'NO2', 'CO2','MASS_PM10']
db_total = pd.read_csv('../media_mobile/tot_media_mobile.csv')
db_total = db_total.drop(columns = ['Unnamed: 0'])
to_remove = ['23/01/2024', '27/01/2024', '29/01/2024', '30/01/2024', '31/01/2024']
for elem in to_remove:
	db_total = db_total.loc[db_total['DATE'] != elem].reset_index(drop=True)
db_total['HOUR'] = db_total['TIME'].str[:2]
max_min_per_colonna = {}
for colonna in colonne:
	db_total[colonna] = pd.to_numeric(db_total[colonna], errors='ignore')
	massimo = db_total[colonna].max()
	minimo = db_total[colonna].min()
	max_min_per_colonna[colonna] = [minimo, massimo]

# days = ['22_01', '24_01', '25_01', '26_01', '28_01', '01_02',
# '04_02','05_02','07_02','08_02','09_02','10_02','12_02','13_02',
# '14_02','15_02','16_02','18_02']
days = ['22_01','24_01', '25_01', '26_01', '28_01', '01_02',
'04_02','05_02','07_02','08_02','09_02','10_02','12_02','13_02',
'14_02','15_02','16_02','18_02']
mf = []
c = 0
for d in range(len(days)):
	mf_d = []
	db_day = pd.read_csv('../media_mobile/'+days[d]+'.csv')
	db_day = db_day.drop(columns = ['Unnamed: 0'])
	db_day['HOUR'] = db_day['TIME'].str[:2]
	hours = sorted(set(db_day['HOUR']))
	for hour in range(len(hours)):
		multiframe = str(days[d])+'_'+str(hours[hour])
		mf_temp = [multiframe for i in range(len(db_day[db_day['HOUR'] == hours[hour]]))]
		mf += mf_temp
		mf_d += mf_temp
	c += len(db_day)
	db_day['multiframe'] = mf_d
import pdb; pdb.set_trace()
db_total['multiframe'] = mf
graph = ox.graph_from_point(monte, dist = radius, network_type = 'walk')
nodes= ox.graph_to_gdfs(graph, nodes=True, edges=False)
edges= ox.graph_to_gdfs(graph, edges=True, nodes=False)
multiframes = db_total['multiframe']
ordered_dict = OrderedDict()
ord_multiframes = []
for valore in multiframes:
	if valore not in ordered_dict:
		ordered_dict[valore] = None
		ord_multiframes.append(valore)
for colonna in colonne:
	db_new_list = []
	for m in range(len(ord_multiframes)):
		db_new_list.append(db_total[db_total['multiframe'] == ord_multiframes[m]])
		db_new = pd.concat(db_new_list, ignore_index=True)
		fig, ax = ox.plot_graph(graph, node_color='white', node_size = 1, close = False, show = False)
		for index, row in db_new.iterrows():
			ax.scatter(row['longitude'], row['latitude'], c=row[colonna],vmin = max_min_per_colonna[colonna][0], vmax= max_min_per_colonna[colonna][1], s=5)
		smap = ScalarMappable(cmap='viridis', norm=plt.Normalize(vmin=max_min_per_colonna[colonna][0], vmax=max_min_per_colonna[colonna][1]))
		cbar = plt.colorbar(smap, ax=ax, orientation='vertical')
		for label in cbar.ax.yaxis.get_ticklabels():
			label.set_color('black')
		cbar.set_label('Value', color='black')
		ax.set_xlabel('Longitude')
		ax.set_ylabel('Latitude')
		plt.title(colonna + ': '+ ord_multiframes[m])
		plt.savefig('plot/tot_multiframe/'+colonna+'_'+ord_multiframes[m]+'.png', bbox_inches='tight', pad_inches=0.05, dpi=300)
		plt.clf()
		plt.close()
		print(ord_multiframes[m])
	print(colonna)

