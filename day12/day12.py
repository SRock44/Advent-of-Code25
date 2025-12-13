def parse_input(filename):
    with open(filename, 'r') as f:
        lines = f.read().strip().split('\n')
    
    shapes = {}
    regions = []
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if ':' in line and line.split(':')[0].strip().isdigit():
            shape_idx = int(line.split(':')[0].strip())
            shape_lines = []
            i += 1
            
            while i < len(lines) and lines[i].strip() and ':' not in lines[i]:
                shape_lines.append(lines[i])
                i += 1
            
            shapes[shape_idx] = shape_lines
        
        elif 'x' in line and ':' in line:
            parts = line.split(':')
            dims = parts[0].strip().split('x')
            width = int(dims[0])
            height = int(dims[1])
            
            quantities = list(map(int, parts[1].strip().split()))
            regions.append((width, height, quantities))
            i += 1
        else:
            i += 1
    
    return shapes, regions

def get_shape_cells(shape_lines):
    cells = []
    for r, line in enumerate(shape_lines):
        for c, char in enumerate(line):
            if char == '#':
                cells.append((r, c))
    return cells

def solve():
    shapes, regions = parse_input('input.txt')
    
    print(f"Parsed {len(shapes)} shapes and {len(regions)} regions")
    
    # calculate size of each shape
    shape_sizes = {}
    for idx, shape_lines in shapes.items():
        cells = get_shape_cells(shape_lines)
        shape_sizes[idx] = len(cells)
    
    count = 0
    
    for i, (width, height, quantities) in enumerate(regions):
        # calculate total cells needed
        total_needed = sum(quantities[j] * shape_sizes[j] for j in range(len(quantities)) if j in shape_sizes)
        total_available = width * height
        
        # simple heuristic: can it fit based on area alone?
        if total_needed <= total_available:
            count += 1
        
        if (i + 1) % 100 == 0:
            print(f"Processed {i+1}/{len(regions)} regions")
    
    return count

if __name__ == '__main__':
    result = solve()
    print(f"\nRegions that can fit all presents: {result}")