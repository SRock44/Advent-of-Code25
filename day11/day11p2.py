from collections import defaultdict, deque

def parse_input(filename):
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

def count_all_paths(graph, start, end):
    """
    count all paths from start to end using dynamic programming
    """
    # dp[node] = number of ways to reach this node from start
    dp = defaultdict(int)
    dp[start] = 1
    
    # topological sort using DFS
    visited = set()
    stack = []
    
    def topo_sort(node):
        if node in visited:
            return
        visited.add(node)
        if node in graph:
            for neighbor in graph[node]:
                topo_sort(neighbor)
        stack.append(node)
    
    topo_sort(start)
    stack.reverse()
    
    # compute paths in topological order
    for node in stack:
        if node == start:
            continue
        if node in graph:
            # this node is reachable from any node that points to it
            for prev_node in graph:
                if node in graph[prev_node]:
                    dp[node] += dp[prev_node]
    
    return dp[end]

def solve_part2():
    graph = parse_input('input.txt')
    
    print(f"Graph loaded. Number of nodes: {len(graph)}")
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def count(node, visited_dac, visited_fft):
        if node == 'out':
            return 1 if visited_dac and visited_fft else 0
        
        if node not in graph:
            return 0
        
        new_dac = visited_dac or (node == 'dac')
        new_fft = visited_fft or (node == 'fft')
        
        total = 0
        for neighbor in graph[node]:
            total += count(neighbor, new_dac, new_fft)
        
        return total
    
    result = count('svr', False, False)
    return result

if __name__ == '__main__':
    result = solve_part2()
    print(f"Number of paths: {result}")