# Allen Rehkemper
# MS549 Module 7.1 Graphing
# Dr. Jill Coddington
# 12/13/2024   
# This project reviews graphing in terms of data structures. 
# The idea is to highlight three algorithms, with at least one pathfinding algorithm in a real-world
# example and utilize a program's graphing capabilities to output a graph based on weight.

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors

# Create the Graph
G = nx.Graph()

# Node Definitions by airport ICAO identifiers
airports = [
    "ATL", "LAX", "ORD", "DFW", "DEN", "JFK", "SFO", "SEA", "LAS", "MCO",
    "MIA", "PHX", "CLT", "EWR", "MSP", "BOS", "IAH", "DCA", "SAN", "PDX"
]

# Define Edges (paths between airports)
connections = [
    ("ATL", "LAX"), ("ATL", "JFK"), ("LAX", "DEN"), ("ORD", "DFW"), ("DFW", "LAS"),
    ("DEN", "SFO"), ("JFK", "SEA"), ("SFO", "SEA"), ("SEA", "LAS"), ("LAS", "MCO"),
    ("MCO", "MIA"), ("MIA", "PHX"), ("PHX", "CLT"), ("CLT", "EWR"), ("EWR", "MSP"),
    ("MSP", "BOS"), ("BOS", "IAH"), ("IAH", "DCA"), ("DCA", "SAN"), ("SAN", "PDX")
]

# Add nodes and edges to the graph
G.add_nodes_from(airports)
G.add_edges_from(connections)

# Add Edge Attributes (Approximate Distances in Statute Miles) https://www.airmilescalculator.com/
distances = {
    ("ATL", "LAX"): 1946, ("ATL", "JFK"): 761, ("LAX", "DEN"): 862, ("ORD", "DFW"): 802,
    ("DFW", "LAS"): 1055, ("DEN", "SFO"): 967, ("JFK", "SEA"): 2422, ("SFO", "SEA"): 679,
    ("SEA", "LAS"): 867, ("LAS", "MCO"): 2039, ("MCO", "MIA"): 192, ("MIA", "PHX"): 1972,
    ("PHX", "CLT"): 1774, ("CLT", "EWR"): 529, ("EWR", "MSP"): 1004, ("MSP", "BOS"): 1122,
    ("BOS", "IAH"): 1595, ("IAH", "DCA"): 1211, ("DCA", "SAN"): 2308, ("SAN", "PDX"): 1007
}
nx.set_edge_attributes(G, distances, "distance")

#  Degree Centrality Coloring
degree_centrality = nx.degree_centrality(G)
centrality_values = list(degree_centrality.values())
norm = colors.Normalize(vmin=min(centrality_values), vmax=max(centrality_values))
colormap = cm.get_cmap('viridis')
node_colors = [colormap(norm(degree_centrality[node])) for node in G.nodes()]

# Node position
pos = nx.spring_layout(G)  

# Visualization Code and edge placement
fig, ax = plt.subplots(figsize=(12, 9))
# Layout for node positions
pos = nx.spring_layout(G)  

# Draw the graph
nx.draw(
    G, pos, with_labels=True, node_color=node_colors, node_size=500,
    font_size=10, edge_color="gray", alpha=0.6, ax=ax
)

# Calculate edge labels
edge_labels = {(u, v): f"{d['distance']} mi" for u, v, d in G.edges(data=True)}

# Adjust edge label positions with an offset
for (u, v), label in edge_labels.items():
    x = (pos[u][0] + pos[v][0]) / 2  # Midpoint X
    y = (pos[u][1] + pos[v][1]) / 2 + 0.03  # Midpoint Y with vertical offset
    plt.text(x, y, label, fontsize=8, color='black', ha='center')

# Add the colorbar for degree of centrality
sm = plt.cm.ScalarMappable(cmap=colormap, norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax)
cbar.set_label("Degree Centrality")

plt.title("Aviation Network Colored by Degree Centrality")
plt.show()


# Pathfinding using Dijkstra's Algorithm
source, target = "ATL", "LAX"
shortest_path = nx.shortest_path(G, source=source, target=target, weight="distance")
shortest_distance = nx.shortest_path_length(G, source=source, target=target, weight="distance")
print("Shortest Pathfinding (Dijkstra's Algorithm):")
print(f"Shortest path from {source} to {target}: {shortest_path}")
print(f"Shortest distance: {shortest_distance} miles\n")

# Analyze Centrality
betweenness_centrality = nx.betweenness_centrality(G, weight="distance")
closeness_centrality = nx.closeness_centrality(G, distance="distance")

most_connected = max(degree_centrality, key=degree_centrality.get)
most_influential = max(betweenness_centrality, key=betweenness_centrality.get)
most_accessible = max(closeness_centrality, key=closeness_centrality.get)

print("Centrality Analysis:")
print(f"Most connected airport (degree centrality): {most_connected}")
print(f"Most influential airport (betweenness centrality): {most_influential}")
print(f"Most accessible airport (closeness centrality): {most_accessible}\n")

# Connectivity Analysis
is_connected = nx.is_connected(G)
connected_components = list(nx.connected_components(G))

print("Connectivity Analysis:")
print(f"Is the network fully connected? {'Yes' if is_connected else 'No'}")
print(f"Number of connected components: {len(connected_components)}")
