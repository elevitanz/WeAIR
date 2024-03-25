import numpy as np
import osmnx as ox
import pandas as pd
import networkx as nx
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

### DA RETE A HEATMAP: PLOT TOTALE NEUTRA
monte = (43.321227, 11.330898)
radius = 5000

db_total = pd.read_csv('../media_mobile/tot_media_mobile.csv')
db_total = db_total.drop(columns = ['Unnamed: 0'])
with open('my_list.csv', 'r') as file:
    lines = file.readlines()
data = [line.replace('"', '').strip().split(',') for line in lines]
for i in range(1,len(data)):
	if len(data[i]) > 2:
		for elem in data[i]:
			if elem == '':
				data[i] = [x for x in data[i] if x != elem]
df = pd.DataFrame(data, columns=['latitude', 'longitude'])
df = df[1:]
df.reset_index(inplace=True)
df = df.drop(columns = ['index'])
df['latitude'] = df['latitude'].astype(float)
df['longitude'] = df['longitude'].astype(float)
df_differenze = df.drop_duplicates()

graph = ox.graph_from_point(monte, dist = radius, network_type = 'walk')
nodes= ox.graph_to_gdfs(graph, nodes=True, edges=False)
edges= ox.graph_to_gdfs(graph, edges=True, nodes=False)
fig, ax = ox.plot_graph(graph, node_color='white', node_size = 3, close = False, show = False)
for index, row in db_total.iterrows():
	ax.scatter(row['longitude'], row['latitude'], color='red', s=5)
for index, row in df_differenze.iterrows():
	ax.scatter(df_differenze['longitude'], df_differenze['latitude'], color = 'lime', s = 20)
# print(df['longitude'][0], df['latitude'][0])
# ax.scatter(df['longitude'][0], df['latitude'][0], color = 'lime', s = 20)
#plt.show()
plt.savefig('plot/new_new_loc_tot.png', bbox_inches='tight', pad_inches=0.05, dpi=600)
plt.clf()
plt.close()
