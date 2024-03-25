import numpy as np
import osmnx as ox
import pandas as pd
import networkx as nx
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

### MAPPA GIORNO PER GIORNO
### ATTENZIONE ALLE DIRECTORY DEI FILE SIA IN LETTURA CHE IN SCRITTURA 
monte = (43.321227, 11.330898)
radius = 10000 ## DI SOLITO E' 5000
days = ['22_01','24_01', '25_01', '26_01', '28_01', '01_02',
'04_02','05_02','07_02','08_02','09_02','10_02','12_02','13_02',
'14_02','15_02','16_02','18_02']
## DA QUI IN POI PER SISTEMARE I DATI PREDETTI
with open("PredictionsMeanOfDay.txt", "r") as file:
    lines = file.readlines()
data = {}
for i in range(0, len(lines), 6):
	d_values = lines[i+2].strip()
	l_values = lines[i+4].strip()
	data[d_values] = l_values

for key, value in data.items():
    coords = value.strip('[]').split()
    coords = [float(coord) for coord in coords]
    data[key] = coords
df = pd.DataFrame(data).T.reset_index()
df.columns = ['day', 'latitude','longitude']
## DA QUI IN POI CICLO SUI GIORNI PER FARE LE MAPPE CON I VARI DATI MOBILI (IN ROSSO) E I DATI PREDETTI (IN VERDE)
for d in days:
	graph = ox.graph_from_point(monte, dist = radius, network_type = 'walk')
	nodes= ox.graph_to_gdfs(graph, nodes=True, edges=False)
	edges= ox.graph_to_gdfs(graph, edges=True, nodes=False)
	fig, ax = ox.plot_graph(graph, node_color='white', node_size = 3, close = False, show = False)
	db_total = pd.read_csv('../media_mobile/'+d+'.csv')
	db_total = db_total.drop(columns = ['Unnamed: 0'])
	for index, row in db_total.iterrows():
		ax.scatter(row['longitude'], row['latitude'], color='red', s=5)
	ax.scatter(df[df['day']==d]['longitude'].values,df[df['day']==d]['latitude'].values, color = 'lime', s = 50)
	plt.savefig('plot/pred_loc_'+d+'.png', bbox_inches='tight', pad_inches=0.05, dpi=600)
	#plt.show()
	plt.clf()
	plt.close()
	print(d)
