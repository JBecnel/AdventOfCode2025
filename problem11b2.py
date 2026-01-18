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


def count_paths(graph, start, end, visited=None):
    if visited is None:
        visited = set()
    
    if start == end:
        return 1
    
    visited.add(start)
    total = 0
    
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            total += count_paths(graph, neighbor, end, visited.copy())
    
    return total

# Load the graph

def count_paths_through_nodes(graph, node1, node2):
    graph_remove_dac = graph.copy()
    graph_remove_dac.pop(node1)

    graph_remove_fft = graph.copy()
    graph_remove_fft.pop(node2)

    graph_remove_dac_fft = graph.copy()
    graph_remove_dac_fft.pop(node1)
    graph_remove_dac_fft.pop(node2)

    options1 = count_paths(graph_remove_dac_fft, 'svr', node1)
    options1 *=count_paths(graph_remove_fft, node1, node2)
    options1 *= count_paths(graph_remove_dac, node2, "out")

    options2 = count_paths(graph_remove_dac_fft, 'svr', node2)
    options2 *= count_paths(graph_remove_dac, node2, node1)
    options2 *= count_paths(graph_remove_fft, node1, "out")

    return options1+options2

graph = build_graph('input11b.txt')
print(count_paths_through_nodes(graph, "dac", "fft"))

graph = build_graph('input11.txt')
print(count_paths_through_nodes(graph, "dac", "fft"))
#print(graph)