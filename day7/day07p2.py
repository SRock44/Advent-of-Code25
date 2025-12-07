def count_timelines(filename):
    """
    count the number of unique timelines (paths) a quantum tachyon particle takes
    each split creates two independent timelines
    """
    with open(filename, 'r') as f:
        lines = f.read().strip().split('\n')
    
    rows = len(lines)
    cols = len(lines[0]) if rows > 0 else 0
    
    # find starting column
    start_col = -1
    for c in range(cols):
        if lines[0][c] == 'S':
            start_col = c
            break
    
    if start_col == -1:
        return 0
    
    # track timelines as (row, col, path_signature)
    # path_signature is a tuple of decisions made at each splitter
    timelines = [[0] * cols for _ in range(rows)]
    timelines[0][start_col] = 1
    
    # process row by row
    for r in range(rows - 1):
        for c in range(cols):
            if timelines[r][c] == 0:
                continue
            
            paths_here = timelines[r][c]
            next_r = r + 1
            cell = lines[next_r][c]
            
            if cell == '.' or cell == 'S':
                # particle continues straight down
                timelines[next_r][c] += paths_here
            elif cell == '^':
                # particle splits - each incoming path creates two paths
                if c > 0:
                    timelines[next_r][c - 1] += paths_here
                if c < cols - 1:
                    timelines[next_r][c + 1] += paths_here
    
    # count total number of paths that exit the manifold
    # (reached the bottom row)
    total_timelines = sum(timelines[rows - 1])
    
    return total_timelines

def solve_part2():
    return count_timelines('input.txt')

if __name__ == '__main__':
    result = solve_part2()
    print(f"Total timelines: {result}")