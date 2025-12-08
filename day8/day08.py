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
        
        return True
    
    def get_circuit_sizes(self):
        # get sizes of all circuits
        circuit_sizes = defaultdict(int)
        for i in range(len(self.parent)):
            root = self.find(i)
            circuit_sizes[root] = self.size[root]
        return list(circuit_sizes.values())

def solve():
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
    
    # process the 1000 shortest edges (not connections made, but edges considered)
    edges_processed = 0
    while edges_processed < 1000 and edges:
        dist_sq, i, j = heapq.heappop(edges)
        uf.union(i, j)  # try to connect, doesn't matter if already connected
        edges_processed += 1
    
    # get circuit sizes and find three largest
    circuit_sizes = uf.get_circuit_sizes()
    circuit_sizes.sort(reverse=True)
    
    # pad with 1s if needed (for safety)
    while len(circuit_sizes) < 3:
        circuit_sizes.append(1)
    
    # multiply three largest
    result = circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]
    return result

if __name__ == '__main__':
    result = solve()
    print(f"Product of three largest circuits: {result}")