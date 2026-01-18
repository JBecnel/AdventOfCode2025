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
graph = build_graph('sample_input11.txt')
paths = count_paths(graph, 'you', 'out')
print(f"Number of paths from 'you' to 'out': {paths}")


graph = build_graph('input11.txt')
paths = count_paths(graph, 'you', 'out')
print(f"Number of paths from 'you' to 'out': {paths}")
#print(graph)