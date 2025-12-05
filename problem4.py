def compute_valid(grid):   
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            cell = grid[r][c]
            
            if cell == '@':                
                adj_count = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        neighbor = grid[nr][nc]
                        if neighbor == '@':
                            adj_count += 1 
                            
                
                if adj_count < 4:
                    count += 1

    return count

file_name = "sample_input4.txt"
file_name = "input4.txt"
with open(file_name, 'r') as file:
    grid = []
    for line in file:
        line = line.rstrip('\n')
        line = list(line)
        grid.append(line)
    print(grid)
    print(compute_valid(grid))