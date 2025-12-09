def parse_input(filename):
    """
    parse red tile positions
    """
    with open(filename, 'r') as f:
        lines = f.read().strip().split('\n')
    
    tiles = []
    for line in lines:
        if line.strip():
            x, y = map(int, line.split(','))
            tiles.append((x, y))
    
    return tiles

def solve():
    tiles = parse_input('input.txt')
    n = len(tiles)
    
    max_area = 0
    
    # try all pairs of tiles as opposite corners
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = tiles[i]
            x2, y2 = tiles[j]
            
            # calculate rectangle area (inclusive of endpoints)
            # from coordinate a to b includes (b-a+1) tiles
            width = abs(x2 - x1) + 1
            height = abs(y2 - y1) + 1
            
            # only valid rectangles (not just single tiles)
            if width > 1 and height > 1:
                area = width * height
                max_area = max(max_area, area)
    
    return max_area

if __name__ == '__main__':
    result = solve()
    print(f"Largest rectangle area: {result}")