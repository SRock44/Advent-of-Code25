def parse_input(filename):
    with open(filename, 'r') as f:
        lines = f.read().strip().split('\n')
    
    tiles = []
    for line in lines:
        if line.strip():
            x, y = map(int, line.split(','))
            tiles.append((x, y))
    
    return tiles

def build_edges(red_tiles):
    """
    build list of edges connecting consecutive red tiles
    """
    n = len(red_tiles)
    edges = []
    
    for i in range(n):
        x1, y1 = red_tiles[i]
        x2, y2 = red_tiles[(i + 1) % n]
        edges.append((x1, y1, x2, y2))
    
    return edges

def rectangles_intersect(minX, minY, maxX, maxY, edge_x1, edge_y1, edge_x2, edge_y2):
    """
    check if rectangle intersects with edge
    """
    edge_minX = min(edge_x1, edge_x2)
    edge_maxX = max(edge_x1, edge_x2)
    edge_minY = min(edge_y1, edge_y2)
    edge_maxY = max(edge_y1, edge_y2)
    
    # check if rectangles overlap
    if minX < edge_maxX and maxX > edge_minX and minY < edge_maxY and maxY > edge_minY:
        return True
    return False

def solve_part2():
    red_tiles = parse_input('input.txt')
    n = len(red_tiles)
    
    edges = build_edges(red_tiles)
    
    max_area = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = red_tiles[i]
            x2, y2 = red_tiles[j]
            
            if x1 == x2 or y1 == y2:
                continue
            
            min_x = min(x1, x2)
            max_x = max(x1, x2)
            min_y = min(y1, y2)
            max_y = max(y1, y2)
            
            # manhattan distance optimization
            manhattan = abs(x2 - x1) + abs(y2 - y1)
            if manhattan * manhattan <= max_area:
                continue
            
            # check if rectangle intersects with any edge
            intersects = False
            for edge_x1, edge_y1, edge_x2, edge_y2 in edges:
                if rectangles_intersect(min_x, min_y, max_x, max_y, edge_x1, edge_y1, edge_x2, edge_y2):
                    intersects = True
                    break
            
            if not intersects:
                area = (max_x - min_x + 1) * (max_y - min_y + 1)
                if area > max_area:
                    max_area = area
    
    return max_area

if __name__ == '__main__':
    import time
    start = time.time()
    result = solve_part2()
    end = time.time()
    print(f"Largest rectangle area: {result}")
    print(f"Time: {(end - start) * 1000:.2f}ms")