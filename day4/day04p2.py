def count_neighbors(grid, r, c, rows, cols):
    """
    count how many of the 8 neighbors are paper rolls
    """
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    count = 0
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == '@':
                count += 1
    return count

def find_removable_rolls(grid):
    """
    find all rolls that currently have < 4 neighbors
    """
    rows = len(grid)
    cols = len(grid[0])
    removable = []
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                if count_neighbors(grid, r, c, rows, cols) < 4:
                    removable.append((r, c))
    
    return removable

def solve_part2():
    # read the grid from input
    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')
    
    # convert to a mutable grid (list of lists)
    grid = [list(line) for line in lines if line]
    rows = len(grid)
    cols = len(grid[0])
    
    total_removed = 0
    
    # keep removing until we can't remove any more
    while True:
        # find all rolls we can remove right now
        removable = find_removable_rolls(grid)
        
        # if nothing can be removed, we're done
        if not removable:
            break
        
        # remove all accessible rolls
        for r, c in removable:
            grid[r][c] = '.'
        
        total_removed += len(removable)
    
    return total_removed

if __name__ == '__main__':
    result = solve_part2()
    print(f"Total rolls removed: {result}")