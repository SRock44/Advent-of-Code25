def parse_line(line):
    start = line.index('{') + 1
    end = line.index('}')
    joltage_str = line[start:end]
    target = [int(x) for x in joltage_str.split(',')]
    
    buttons = []
    rest = line[:start-1]
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

def solve_machine_ilp(target, buttons):
    try:
        from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpStatus
        import pulp
    except ImportError:
        print("Error: PuLP not installed. Install with: pip install pulp")
        return float('inf')
    
    num_counters = len(target)
    num_buttons = len(buttons)
    
    # create problem
    prob = LpProblem("MinButtonPresses", LpMinimize)
    
    # decision variables (number of times each button is pressed)
    x = [LpVariable(f"x{i}", lowBound=0, cat='Integer') for i in range(num_buttons)]
    
    # objective: minimize total button presses
    prob += lpSum(x)
    
    # constraints: for each counter, sum of button presses must equal target
    for counter in range(num_counters):
        prob += lpSum([x[j] for j in range(num_buttons) if counter in buttons[j]]) == target[counter]
    
    # solve using default solver (PULP_CBC_CMD is usually available)
    try:
        prob.solve(pulp.PULP_CBC_CMD(msg=0))
    except:
        prob.solve()
    
    if LpStatus[prob.status] == 'Optimal':
        return int(sum([x[i].varValue for i in range(num_buttons)]))
    else:
        return float('inf')

def solve():
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, 'input.txt')
    with open(input_path, 'r') as f:
        lines = f.read().strip().split('\n')
    
    total = 0
    for line in lines:
        if not line.strip():
            continue
        
        target, buttons = parse_line(line)
        result = solve_machine_ilp(target, buttons)
        
        if result == float('inf'):
            print(f"No solution for line: {line}")
            return -1
        
        total += result
    
    return total

if __name__ == '__main__':
    result = solve()
    print(f"Minimum button presses: {result}")