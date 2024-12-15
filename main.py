# Allen Rehkemper
# MS549 Module 7.1 Graphing
# Dr. Jill Coddington
# 12/13/2024
# Main execution file for graph creation and analysis.

from graph_utils import create_graph, degree_centrality_coloring, visualize_graph, dijkstra_path, centrality_analysis, connectivity_analysis
import networkx as nx

# Step 1: Define the graph data
airports = [
    "ATL", "LAX", "ORD", "DFW", "DEN", "JFK", "SFO", "SEA", "LAS", "MCO",
    "MIA", "PHX", "CLT", "EWR", "MSP", "BOS", "IAH", "DCA", "SAN", "PDX"
]

connections = [
    ("ATL", "LAX"), ("ATL", "JFK"), ("LAX", "DEN"), ("ORD", "DFW"), ("DFW", "LAS"),
    ("DEN", "SFO"), ("JFK", "SEA"), ("SFO", "SEA"), ("SEA", "LAS"), ("LAS", "MCO"),
    ("MCO", "MIA"), ("MIA", "PHX"), ("PHX", "CLT"), ("CLT", "EWR"), ("EWR", "MSP"),
    ("MSP", "BOS"), ("BOS", "IAH"), ("IAH", "DCA"), ("DCA", "SAN"), ("SAN", "PDX")
]

distances = {
    ("ATL", "LAX"): 1946, ("ATL", "JFK"): 761, ("LAX", "DEN"): 862, ("ORD", "DFW"): 802,
    ("DFW", "LAS"): 1055, ("DEN", "SFO"): 967, ("JFK", "SEA"): 2422, ("SFO", "SEA"): 679,
    ("SEA", "LAS"): 867, ("LAS", "MCO"): 2039, ("MCO", "MIA"): 192, ("MIA", "PHX"): 1972,
    ("PHX", "CLT"): 1774, ("CLT", "EWR"): 529, ("EWR", "MSP"): 1004, ("MSP", "BOS"): 1122,
    ("BOS", "IAH"): 1595, ("IAH", "DCA"): 1211, ("DCA", "SAN"): 2308, ("SAN", "PDX"): 1007
}

# Step 2: Create and visualize the graph
G = create_graph(airports, connections, distances)
degree_centrality, node_colors = degree_centrality_coloring(G)
pos = nx.spring_layout(G)
visualize_graph(G, pos, node_colors, distances)

# Step 3: Pathfinding using Dijkstra's Algorithm
source, target = "ATL", "LAX"
shortest_path, shortest_distance = dijkstra_path(G, source, target)
print("Shortest Pathfinding (Dijkstra's Algorithm):")
print(f"Shortest path from {source} to {target}: {shortest_path}")
print(f"Shortest distance: {shortest_distance} miles\n")

# Step 4: Centrality Analysis
degree, betweenness, closeness = centrality_analysis(G)
most_connected = max(degree, key=degree.get)
most_influential = max(betweenness, key=betweenness.get)
most_accessible = max(closeness, key=closeness.get)

print("Centrality Analysis:")
print(f"Most connected airport (degree centrality): {most_connected}")
print(f"Most influential airport (betweenness centrality): {most_influential}")
print(f"Most accessible airport (closeness centrality): {most_accessible}\n")

# Step 5: Connectivity Analysis
is_connected, components = connectivity_analysis(G)
print("Connectivity Analysis:")
print(f"Is the network fully connected? {'Yes' if is_connected else 'No'}")
print(f"Number of connected components: {len(components)}")
