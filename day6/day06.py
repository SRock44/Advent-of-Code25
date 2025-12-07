def parse_worksheet(filename):
    """
    parse the math worksheet - problems are arranged vertically in columns
    """
    with open(filename, 'r') as f:
        lines = f.read().split('\n')
    
    # remove any trailing empty lines
    while lines and not lines[-1].strip():
        lines.pop()
    
    if not lines:
        return []
    
    # find the width we need to work with
    max_width = max(len(line) for line in lines)
    
    # pad all lines to the same width
    padded_lines = [line.ljust(max_width) for line in lines]
    
    problems = []
    col = 0
    
    # scan through columns to find problems
    while col < max_width:
        # check if this column is all spaces (separator)
        if all(line[col] == ' ' for line in padded_lines):
            col += 1
            continue
        
        # found the start of a problem, collect all columns until next separator
        problem_cols = []
        while col < max_width and not all(line[col] == ' ' for line in padded_lines):
            problem_cols.append(col)
            col += 1
        
        # extract the problem from these columns
        if problem_cols:
            # get all non-empty values from these columns (except last row which is the operator)
            numbers = []
            operator = None
            
            for row_idx, line in enumerate(padded_lines):
                # get the text from this problem's columns
                text = ''.join(line[c] for c in problem_cols).strip()
                
                if text:
                    # last row should be the operator
                    if row_idx == len(padded_lines) - 1:
                        operator = text
                    else:
                        numbers.append(int(text))
            
            if numbers and operator:
                problems.append((numbers, operator))
    
    return problems

def solve_problem(numbers, operator):
    """
    solve a single problem by applying the operator to all numbers
    """
    if operator == '+':
        return sum(numbers)
    elif operator == '*':
        result = 1
        for num in numbers:
            result *= num
        return result
    else:
        raise ValueError(f"unknown operator: {operator}")

def solve():
    problems = parse_worksheet('input.txt')
    
    grand_total = 0
    for numbers, operator in problems:
        answer = solve_problem(numbers, operator)
        grand_total += answer
    
    return grand_total

if __name__ == '__main__':
    result = solve()
    print(f"Grand total: {result}")