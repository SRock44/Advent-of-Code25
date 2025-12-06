# day 1 part 2: count every time dial points at 0 during any rotation

def solve():
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
        
        # count complete circles (every 100 units = 1 pass through 0)
        complete_circles = distance // 100
        count += complete_circles
        
        # handle the remaining partial rotation
        remaining = distance % 100
        
        if direction == 'L':
            # moving counter-clockwise (subtracting)
            # calculate new position
            new_position = (position - distance) % 100
            
            # check if we cross 0 during the partial rotation
            # we cross 0 if: position - remaining < 0, which means position < remaining
            # but NOT if we start at 0 (starting at 0 doesn't count as crossing)
            if position > 0 and position < remaining:
                count += 1
            # if we don't cross 0, check if we end at 0
            elif new_position == 0:
                count += 1
            
            position = new_position
        else:  # direction == 'R'
            # moving clockwise (adding)
            # calculate new position
            new_position = (position + distance) % 100
            
            # check if we cross 0 during the partial rotation
            # we cross 0 if: position + remaining >= 100
            # but NOT if we start at 0 (starting at 0 doesn't count as crossing)
            if position > 0 and position + remaining >= 100:
                count += 1
            # if we don't cross 0, check if we end at 0
            elif new_position == 0:
                count += 1
            
            position = new_position
    
    return count

if __name__ == '__main__':
    result = solve()
    print(f"password: {result}")
