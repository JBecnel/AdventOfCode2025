from pathlib import Path
from itertools import combinations
import heapq


def read_tuples():
    """
    Read sample_input8.txt (or provided filename) line by line.
    Each non-empty line is expected to contain 3 numbers separated by commas.
    Returns a list of 3-tuples (numbers parsed as int or float).
    """
    file_name = "sample_input8.txt"
    #file_name = "input8.txt"
    result = []

    
    with Path(file_name).open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()            
            parts = [p.strip() for p in line.split(",")]
            parts = tuple(int(p) for p in parts)
            result.append(parts)  

    return result

if __name__ == "__main__":
    tuples = read_tuples()
    #print(tuples)

    # Calculate Euclidean distances between all pairs
    distances = []
    for t1, t2 in combinations(range(len(tuples)), 2):
        dist = sum((tuples[t1][i] - tuples[t2][i])**2 for i in range(3))
        heapq.heappush(distances, (dist, t1, t2))

    
    connections = [ ]
    edges_added = 0
    while edges_added < 10 and distances:
        dist, t1, t2 = heapq.heappop(distances)
        
        t1_conn = None
        t2_conn = None
        for i in range(len(connections)):
            conn = connections[i]
            if (t1 in conn):
                t1_conn = conn

            if (t2 in conn):
                t2_conn = conn
            
            if t1_conn and t2_conn:
                break

        if t1_conn and t2_conn and t1_conn != t2_conn:
            t1_conn.update(t2_conn)
            connections.remove(t2_conn)
        elif t1_conn:
            t1_conn.add(t2)
        elif t2_conn:
            t2_conn.add(t1)
        else:       
            connections.append({t1, t2})        
        
        edges_added += 1

    lengths = [len(conn) for conn in connections]
    lengths.sort(reverse=True)
    total = lengths[0] * lengths[1] * lengths[2]
    print("Lengths of largest 3 components:", lengths[:3])
    print("Total combinations:", total)