import numpy as np
import osmnx as ox
import pandas as pd
import networkx as nx
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable


### DA RETE A HEATMAP-MULTIFRAME: PLOT GIORNO PER GIORNO E PER INDICATORE
monte = (43.321227, 11.330898)
#radius = 5000
### CREI UNA COLORMAP TRA min e max PER OGNI COLONNA.

# colonne = ['AMBT']
colonne = ['AMBT', 'AMBH','AMBP', 'CO', 'NO2', 'CO2','MASS_PM10']
db_total = pd.read_csv('../media_mobile/tot_media_mobile.csv')
db_total = db_total.drop(columns = ['Unnamed: 0'])
max_min_per_colonna = {}
for colonna in colonne:
	db_total[colonna] = pd.to_numeric(db_total[colonna], errors='ignore')
	massimo = db_total[colonna].max()
	minimo = db_total[colonna].min()
	max_min_per_colonna[colonna] = [minimo, massimo]

days = ['22_01', '24_01', '25_01', '26_01', '28_01', '01_02', '04_02','05_02','07_02']
for d in days:
	db_total = pd.read_csv('../media_mobile/'+d+'.csv')
	db_total = db_total.drop(columns = ['Unnamed: 0'])
	db_total['HOUR'] = db_total['TIME'].str[:2]
	if d[-1] == '1':
		radius = 5000
	else:
		radius = 1000
	#db_total = db_total.loc[db_total['CH0'] >= 0].reset_index(drop=True)
	graph = ox.graph_from_point(monte, dist = radius, network_type = 'walk')
	nodes= ox.graph_to_gdfs(graph, nodes=True, edges=False)
	edges= ox.graph_to_gdfs(graph, edges=True, nodes=False)
	for colonna in colonne:
		db_new_list = []
		hours = sorted(set(db_total['HOUR']))
		for hour in hours:
			db_new_list.append(db_total[db_total['HOUR'] == hour])
			db_new = pd.concat(db_new_list, ignore_index=True)
			fig, ax = ox.plot_graph(graph, node_color='white', node_size = 1, close = False, show = False)
			for index, row in db_new.iterrows():
				ax.scatter(row['longitude'], row['latitude'], c=row[colonna],vmin = max_min_per_colonna[colonna][0], vmax= max_min_per_colonna[colonna][1], s=5)
			smap = ScalarMappable(cmap='viridis', norm=plt.Normalize(vmin=max_min_per_colonna[colonna][0], vmax=max_min_per_colonna[colonna][1]))
			cbar = plt.colorbar(smap, ax=ax, orientation='vertical')
			for label in cbar.ax.yaxis.get_ticklabels():
				label.set_color('black')
			cbar.set_label('Valore', color='black')
			ax.set_xlabel('Longitude')
			ax.set_ylabel('Latitude')
			plt.title(colonna + ': HOUR '+ hour)
			plt.savefig('plot/multiframe/heat_'+colonna+'_'+d+'_'+hour+'.png', bbox_inches='tight', pad_inches=0.05, dpi=300)
			plt.clf()
			plt.close()
			print(hour)
		print(colonna)
	print(d)
