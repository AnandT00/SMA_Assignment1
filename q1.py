import networkx as nx

G = nx.read_gml('/content/karate.gml', label= 'id')
G2 = nx.read_gml('/content/dolphins.gml')
G3 = nx.read_weighted_edgelist('jazz.net')

#Karate
print('KARATE---------------------------')
print('Number of nodes:',G.number_of_nodes())
print('Number of edges:',G.number_of_edges())
print('Avg shortest path length:',nx.average_shortest_path_length(G))
print('Avg Clustering:',nx.average_clustering(G))
print()

#Dolphins
print('DOLPHINS-------------------------')
print('Number of nodes:',G2.number_of_nodes())
print('Number of edges:',G2.number_of_edges())
print('Avg shortest path length:',nx.average_shortest_path_length(G2))
print('Avg Clustering:',nx.average_clustering(G2))
print()

#Jazz
print('JAZZ-----------------------------')
print('Number of nodes:',G3.number_of_nodes())
print('Number of edges:',G3.number_of_edges())
print('Avg shortest path length:',nx.average_shortest_path_length(G3))
print('Avg Clustering:',nx.average_clustering(G3))