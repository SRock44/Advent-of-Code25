# day 1: secret entrance
# count how many times the dial points at 0 after any rotation

def solve():
    # dial starts at 50
    position = 50
    count = 0
    
    # read input
    with open('input.txt', 'r') as f:
        content = f.read().strip()
    
    # handle both newline-separated and space-separated input
    if '\n' in content:
        rotations = content.split('\n')
    else:
        rotations = content.split()
    
    # filter out empty strings
    rotations = [r for r in rotations if r]
    
    # process each rotation
    for rotation in rotations:
        if not rotation:
            continue
        
        direction = rotation[0]
        distance = int(rotation[1:])
        
        # apply rotation
        if direction == 'L':
            position = (position - distance) % 100
        else:  # direction == 'R'
            position = (position + distance) % 100
        
        # check if we're at 0
        if position == 0:
            count += 1
    
    return count

if __name__ == '__main__':
    result = solve()
    print(f"password: {result}")

