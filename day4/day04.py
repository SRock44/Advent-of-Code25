def count_accessible_rolls(grid):
    """
    count how many paper rolls (@) have fewer than 4 adjacent rolls
    """
    rows = len(grid)
    cols = len(grid[0])
    accessible = 0
    
    # check all 8 directions: up, down, left, right, and 4 diagonals
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    # look at every position in the grid
    for r in range(rows):
        for c in range(cols):
            # only care about paper rolls
            if grid[r][c] != '@':
                continue
            
            # count how many neighbors are also paper rolls
            neighbor_count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # make sure we're still in bounds
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '@':
                        neighbor_count += 1
            
            # if less than 4 neighbors, forklift can reach it
            if neighbor_count < 4:
                accessible += 1
    
    return accessible

def solve():
    # read the grid from input
    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')
    
    # convert to a proper grid (list of strings works fine)
    grid = [line for line in lines if line]
    
    result = count_accessible_rolls(grid)
    return result

if __name__ == '__main__':
    result = solve()
    print(f"Accessible paper rolls: {result}")