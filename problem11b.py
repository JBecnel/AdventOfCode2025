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


def find_paths(graph, start, end, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    
    path = path + [start]
    visited.add(start)
    
    if start == end:
        return [path]
    
    all_paths = []
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            new_paths = find_paths(graph, neighbor, end, visited.copy(), path)
            all_paths.extend(new_paths)
    
    return all_paths

# Load the graph
graph = build_graph('input11b.txt')
paths = find_paths(graph, 'svr', 'out')
total = 0
print(paths)
for p in paths:
    if "dac" in p and "fft" in p:
        total = total + 1
print(f"Number of paths from 'svr' to 'out': {total}")


graph = build_graph('input11.txt')
paths = find_paths(graph, 'svr', 'out')
total = 0
print(len(paths))
for p in paths:
    if "dac" in p and "fft" in p:
        total = total + 1
print(f"Number of paths from 'svr' to 'out': {total}")
#print(graph)