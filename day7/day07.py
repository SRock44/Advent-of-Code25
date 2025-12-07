def parse_manifold(filename):
    """
    parse the manifold diagram into a grid
    """
    with open(filename, 'r') as f:
        lines = f.read().strip().split('\n')
    
    grid = [list(line) for line in lines]
    return grid

def find_start(grid):
    """
    find the starting position marked with 'S'
    """
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'S':
                return (r, c)
    return None

def simulate_beams(grid):
    """
    simulate the tachyon beams moving downward and splitting
    returns the total number of splits
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # find starting position
    start = find_start(grid)
    if not start:
        return 0
    
    # track active beams as (row, col) positions
    # beams always move downward
    beams = [start]
    split_count = 0
    
    # keep track of positions we've already processed to avoid infinite loops
    # (though in this problem beams just move down and exit)
    processed = set()
    
    while beams:
        new_beams = []
        
        for r, c in beams:
            # move beam down one step
            next_r = r + 1
            
            # check if beam exits the manifold
            if next_r >= rows:
                continue
            
            # check what's at the next position
            next_cell = grid[next_r][c]
            
            if next_cell == '.':
                # beam continues straight down
                new_beams.append((next_r, c))
            elif next_cell == '^':
                # beam hits a splitter - stop this beam and create two new ones
                # only count the split if we haven't processed this splitter from this position before
                if (next_r, c) not in processed:
                    split_count += 1
                    processed.add((next_r, c))
                    
                    # create beams to the left and right
                    if c - 1 >= 0:
                        new_beams.append((next_r, c - 1))
                    if c + 1 < cols:
                        new_beams.append((next_r, c + 1))
            elif next_cell == 'S':
                # shouldn't happen but treat as empty space
                new_beams.append((next_r, c))
        
        beams = new_beams
    
    return split_count

def solve():
    grid = parse_manifold('input.txt')
    return simulate_beams(grid)

if __name__ == '__main__':
    result = solve()
    print(f"Total beam splits: {result}")