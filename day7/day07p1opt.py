def simulate_beams_optimized(filename):
    """
    optimized solution for day 7 part 1; my first attempt was too slow.
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
    
    # track active beams per row as a set of column positions
    # start with one beam at the starting column
    active_beams = {start_col}
    split_count = 0
    
    # process row by row moving downward
    for r in range(1, rows):
        next_beams = set()
        
        for c in active_beams:
            cell = lines[r][c]
            
            if cell == '.':
                # beam continues straight down
                next_beams.add(c)
            elif cell == '^':
                # beam splits - count it and create left/right beams
                split_count += 1
                if c > 0:
                    next_beams.add(c - 1)
                if c < cols - 1:
                    next_beams.add(c + 1)
            # if cell is 'S', treat as empty and continue
            elif cell == 'S':
                next_beams.add(c)
        
        active_beams = next_beams
        
        # early exit if no more active beams
        if not active_beams:
            break
    
    return split_count

def solve():
    return simulate_beams_optimized('input.txt')

if __name__ == '__main__':
    result = solve()
    print(f"Total beam splits: {result}")