import heapq
from collections import defaultdict

def parse_input(filename):
    """
    parse junction box positions
    """
    with open(filename, 'r') as f:
        lines = f.read().strip().split('\n')
    
    boxes = []
    for line in lines:
        if line.strip():
            x, y, z = map(int, line.split(','))
            boxes.append((x, y, z))
    
    return boxes

def distance_squared(box1, box2):
    """
    calculate squared euclidean distance (avoid sqrt for speed)
    """
    dx = box1[0] - box2[0]
    dy = box1[1] - box2[1]
    dz = box1[2] - box2[2]
    return dx*dx + dy*dy + dz*dz

class UnionFind:
    """
    union-find (disjoint set) data structure for tracking connected circuits
    """
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_components = n
    
    def find(self, x):
        # path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        # union by size
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False  # already connected
        
        # attach smaller tree under larger tree
        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        
        self.num_components -= 1
        return True
    
    def is_fully_connected(self):
        return self.num_components == 1

def solve_part2():
    boxes = parse_input('input.txt')
    n = len(boxes)
    
    # create priority queue of all pairs and their distances
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist_sq = distance_squared(boxes[i], boxes[j])
            heapq.heappush(edges, (dist_sq, i, j))
    
    # use union-find to track circuits
    uf = UnionFind(n)
    
    last_connection = None
    
    # keep connecting until everything is in one circuit
    while not uf.is_fully_connected() and edges:
        dist_sq, i, j = heapq.heappop(edges)
        if uf.union(i, j):
            # this was a successful connection
            last_connection = (i, j)
    
    if last_connection:
        i, j = last_connection
        x1, y1, z1 = boxes[i]
        x2, y2, z2 = boxes[j]
        result = x1 * x2
        return result
    
    return 0

if __name__ == '__main__':
    result = solve_part2()
    print(f"Product of X coordinates: {result}")