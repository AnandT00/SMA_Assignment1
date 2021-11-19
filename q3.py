import q2
import networkx as nx

G = nx.read_gml('/content/karate.gml', label= 'id')
G2 = nx.read_gml('/content/dolphins.gml')
G3 = nx.read_weighted_edgelist('jazz.net')

#Karate
print('KARATE---------------------------')
modular, sets = q2.grivan_newman_algo(G)
print('betweenness based clustering (using grivan newman)')
print('modularity:', modular)
print('Number of clusters:', len(sets))
print('Clusters:', sets)
print()

modular2, sets2 = q2.modularity_based_algo(G)
print('modularity based clustering')
print('modularity:', modular2)
print('Number of clusters:', len(sets2))
print('Clusters:', sets2)
print()

modular3, sets3 = q2.spectral_clustering_algo(G)
print('spectral clustering (using laplacian)')
print('modularity:', modular3)
print('Number of clusters:', len(sets3))
print('Clusters:', sets3)
print()

#Dolphins
print('DOLPHINS-------------------------')
modular, sets = q2.grivan_newman_algo(G2)
print('betweenness based clustering (using grivan newman)')
print('modularity:', modular)
print('Number of clusters:', len(sets))
print('Clusters:', sets)
print()

modular2, sets2 = q2.modularity_based_algo(G2)
print('modularity based clustering')
print('modularity:', modular2)
print('Number of clusters:', len(sets2))
print('Clusters:', sets2)
print()

modular3, sets3 = q2.spectral_clustering_algo(G2)
print('spectral clustering (using laplacian)')
print('modularity:', modular3)
print('Number of clusters:', len(sets3))
print('Clusters:', sets3)
print()

#Jazz
print('JAZZ-----------------------------')
modular, sets = q2.grivan_newman_algo(G3)
print('betweenness based clustering (using grivan newman)')
print('modularity:', modular)
print('Number of clusters:', len(sets))
print('Clusters:', sets)
print()

modular2, sets2 = q2.modularity_based_algo(G3)
print('modularity based clustering')
print('modularity:', modular2)
print('Number of clusters:', len(sets2))
print('Clusters:', sets2)
print()

modular3, sets3 = q2.spectral_clustering_algo(G3)
print('spectral clustering (using laplacian)')
print('modularity:', modular3)
print('Number of clusters:', len(sets3))
print('Clusters:', sets3)