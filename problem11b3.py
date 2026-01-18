import networkx as nx
from collections import deque
from functools import cache

def build_graph(filename):
    graph = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(':')
            start = parts[0].strip()
            destinations = parts[1].strip().split()
            graph[start] = destinations
    return graph

graph = build_graph('input11.txt')

# import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add edges from the graph dictionary
for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# # Create visualization
# plt.figure(figsize=(12, 8))
# pos = nx.spring_layout(G, k=2, iterations=50)
# nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
# nx.draw_networkx_labels(G, pos, font_size=8)
# nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True, arrowsize=20)

# plt.title("Graph Visualization")
# plt.axis('off')
# plt.tight_layout()
# # Use planar layout with custom positioning
# pos = nx.spring_layout(G, k=2, iterations=50)

# # Adjust positions to place "svr" on left and "out" on right
# if "svr" in pos:
#     pos["svr"] = [-2, 0]
# if "out" in pos:
#     pos["out"] = [2, 0]

# plt.figure(figsize=(14, 8))
# nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
# nx.draw_networkx_labels(G, pos, font_size=8)
# nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True, arrowsize=20)

# plt.title("Graph Visualization")
# plt.axis('off')
# plt.tight_layout()
# plt.show()

def count_paths(start, end, dac_flag, fft_flag):
    
    
    @cache    
    def dfs(current_node, dac_flag, fft_flag):
        if current_node == end:            
            return 1 if (dac_flag and fft_flag) else 0
        
        if current_node == "dac":
            dac_flag = True
        elif current_node == "fft":
            fft_flag = True

        if current_node in graph:
            total = 0
            for neighbor in graph[current_node]:                
                total += dfs(neighbor, dac_flag, fft_flag)
            return total
        return 0

    return dfs(start, False, False)
    
  
   

# Load the graph



graph = build_graph('input11b.txt')
print(count_paths("svr", "out", False, False))
print()
graph = build_graph('input11.txt')
print(count_paths("svr", "out", False, False))
