import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])
nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray", node_size=2000)
plt.show()
