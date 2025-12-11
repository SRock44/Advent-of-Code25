def parse_input(filename):
    """
    parse the device connections into a graph
    """
    graph = {}
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            parts = line.split(':')
            device = parts[0].strip()
            
            if len(parts) > 1:
                outputs = parts[1].strip().split()
                graph[device] = outputs
            else:
                graph[device] = []
    
    return graph

def count_paths(graph, start, end, visited=None):
    """
    count all paths from start to end using dfs
    """
    if visited is None:
        visited = set()
    
    # base case: reached the end
    if start == end:
        return 1
    
    # if node not in graph or already visited (cycle detection)
    if start not in graph or start in visited:
        return 0
    
    # mark as visited
    visited.add(start)
    
    # count paths through all neighbors
    total_paths = 0
    for neighbor in graph[start]:
        total_paths += count_paths(graph, neighbor, end, visited)
    
    # backtrack - remove from visited so other paths can use this node
    visited.remove(start)
    
    return total_paths

def solve():
    graph = parse_input('input.txt')
    
    # count paths from 'you' to 'out'
    num_paths = count_paths(graph, 'you', 'out')
    
    return num_paths

if __name__ == '__main__':
    result = solve()
    print(f"Number of paths from 'you' to 'out': {result}")