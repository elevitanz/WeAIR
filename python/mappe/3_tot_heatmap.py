import numpy as np
import osmnx as ox
import pandas as pd
import networkx as nx
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable

### DA RETE A HEATMAP: PLOT TOTALE E PER INDICATORE
monte = (43.321227, 11.330898)
radius = 5000
### CREI UNA COLORMAP TRA min e max PER OGNI COLONNA.
### SE CI SONO SOVRAPPOSIZIONI PRENDI IL MAX

colonne = ['MASS_PM10','AMBT', 'AMBH','AMBP', 'CO', 'NO2', 'CO2']
# colonne = ['AMBT']
db_total = pd.read_csv('../media_mobile/tot_media_mobile.csv')
db_total = db_total.drop(columns = ['Unnamed: 0'])
max_min_per_colonna = {}
for colonna in colonne:
	db_total[colonna] = pd.to_numeric(db_total[colonna], errors='ignore')
	massimo = db_total[colonna].max()
	minimo = db_total[colonna].min()
	max_min_per_colonna[colonna] = [minimo, massimo]
graph = ox.graph_from_point(monte, dist = radius, network_type = 'walk')
nodes= ox.graph_to_gdfs(graph, nodes=True, edges=False)
edges= ox.graph_to_gdfs(graph, edges=True, nodes=False)
for colonna in colonne:
	fig, ax = ox.plot_graph(graph, node_color='white', node_size = 1, close = False, show = False)
	for index, row in db_total.iterrows():
		ax.scatter(row['longitude'], row['latitude'], c=row[colonna],vmin = max_min_per_colonna[colonna][0], vmax= max_min_per_colonna[colonna][1], s=5)
	smap = ScalarMappable(cmap='viridis', norm=plt.Normalize(vmin=max_min_per_colonna[colonna][0], vmax=max_min_per_colonna[colonna][1]))
	cbar = plt.colorbar(smap, ax=ax, orientation='vertical')
	for label in cbar.ax.yaxis.get_ticklabels():
		label.set_color('black')
	cbar.set_label('Value', color='black')
	ax.set_xlabel('Longitude')
	ax.set_ylabel('Latitude')
	plt.savefig('plot/tot_heat_'+colonna+'.png', bbox_inches='tight', pad_inches=0.05, dpi=600)
	plt.clf()
	plt.close()
	print(colonna)
