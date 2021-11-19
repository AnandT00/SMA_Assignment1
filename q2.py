import networkx as nx
import itertools
import numpy as np
from sklearn.cluster import SpectralClustering
np.random.seed(1)

def grivan_newman_algo(G):
  iter = nx.algorithms.community.centrality.girvan_newman(G)
  k = 16
  modul_max = 0
  j = 0
  final = []
  for communities in itertools.islice(iter, k):
    modul = nx.algorithms.community.quality.modularity(G, communities)
    if modul > modul_max:
      modul_max = modul
      j = len(communities)
      final = communities

  return modul_max, final

def modularity_based_algo(G):
  sets = nx.algorithms.community.modularity_max.greedy_modularity_communities(G)
  modul = nx.algorithms.community.quality.modularity(G, sets)
  return modul, sets

def spectral_clustering_algo(G):
  adj_mat = nx.to_numpy_matrix(G)


  # Cluster
  modul_max = 0
  j = 0

  for i in range(2, 10):
    sc = SpectralClustering(i, affinity='precomputed', n_init=100)
    sc.fit(np.asarray(adj_mat))

    dict1 = {}
    temp = list(G.nodes)
    for i in range(len(G.nodes)):
      label = sc.labels_[i]
      if label in dict1:
        dict1[label].append(temp[i])
      else:
        dict1[label] = [temp[i]]

    fin = []
    for value in dict1.values():
      fin.append(value)

    
    modul = nx.algorithms.community.quality.modularity(G, fin)
    if modul > modul_max:
      modul_max = modul
      final_set = fin

  return modul_max, final_set