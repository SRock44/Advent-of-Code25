# i almost gave up on this one.
def parse_line(line):
    start = line.index('[') + 1
    end = line.index(']')
    lights = line[start:end]
    target = [1 if c == '#' else 0 for c in lights]
    
    buttons = []
    rest = line[end+1:]
    i = 0
    while i < len(rest):
        if rest[i] == '(':
            close = rest.index(')', i)
            button_str = rest[i+1:close]
            if button_str:
                button = [int(x) for x in button_str.split(',')]
                buttons.append(button)
            i = close + 1
        else:
            i += 1
    
    return target, buttons

def solve_machine(target, buttons):
    num_lights = len(target)
    num_buttons = len(buttons)
    
    # build matrix: rows = lights, cols = buttons
    A = []
    for i in range(num_lights):
        row = []
        for button in buttons:
            row.append(1 if i in button else 0)
        A.append(row)
    
    # augmented matrix
    for i in range(num_lights):
        A[i].append(target[i])
    
    # gaussian elimination over gf(2)
    pivot_col = []
    row = 0
    
    for col in range(num_buttons):
        # find pivot
        pivot_row = -1
        for r in range(row, num_lights):
            if A[r][col] == 1:
                pivot_row = r
                break
        
        if pivot_row == -1:
            continue
        
        # swap rows
        A[row], A[pivot_row] = A[pivot_row], A[row]
        pivot_col.append(col)
        
        # eliminate
        for r in range(num_lights):
            if r != row and A[r][col] == 1:
                for c in range(num_buttons + 1):
                    A[r][c] ^= A[row][c]
        
        row += 1
    
    # check consistency
    for r in range(row, num_lights):
        if A[r][num_buttons] == 1:
            return float('inf')
    
    # find minimum solution
    free_vars = [c for c in range(num_buttons) if c not in pivot_col]
    min_presses = float('inf')
    
    for mask in range(1 << len(free_vars)):
        sol = [0] * num_buttons
        
        for i, v in enumerate(free_vars):
            sol[v] = (mask >> i) & 1
        
        for i in range(len(pivot_col) - 1, -1, -1):
            col = pivot_col[i]
            for r in range(num_lights):
                if A[r][col] == 1:
                    val = A[r][num_buttons]
                    for c in range(col + 1, num_buttons):
                        val ^= A[r][c] * sol[c]
                    sol[col] = val
                    break
        
        min_presses = min(min_presses, sum(sol))
    
    return min_presses

def solve():
    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')
    
    total = 0
    for line in lines:
        target, buttons = parse_line(line)
        result = solve_machine(target, buttons)
        total += result
    
    return total

if __name__ == '__main__':
    print(f"Minimum button presses: {solve()}")