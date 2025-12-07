def parse_worksheet_rtl(filename):
    """
    parse the math worksheet - read right-to-left, with digits in each column
    forming numbers from top to bottom
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
    
    # process columns from right to left
    col = max_width - 1
    
    while col >= 0:
        # skip separator columns (all spaces)
        if all(line[col] == ' ' for line in padded_lines):
            col -= 1
            continue
        
        # found a problem - collect columns moving left until we hit a separator
        problem_cols = []
        while col >= 0 and not all(line[col] == ' ' for line in padded_lines):
            problem_cols.append(col)
            col -= 1
        
        # we collected columns right-to-left, but within a problem
        # we process them left-to-right, so reverse
        problem_cols.reverse()
        
        # extract the problem from these columns
        if problem_cols:
            numbers = []
            operator = None
            
            # each column is a separate number (read top to bottom)
            for col_idx in problem_cols:
                digits = []
                for row_idx, line in enumerate(padded_lines):
                    char = line[col_idx]
                    
                    # last row should be the operator
                    if row_idx == len(padded_lines) - 1:
                        if char.strip():
                            operator = char
                    else:
                        # collect digits for this number
                        if char.strip():
                            digits.append(char)
                
                # form the number from the digits (top to bottom)
                if digits:
                    number = int(''.join(digits))
                    numbers.append(number)
            
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

def solve_part2():
    problems = parse_worksheet_rtl('input.txt')
    
    grand_total = 0
    for numbers, operator in problems:
        answer = solve_problem(numbers, operator)
        grand_total += answer
    
    return grand_total

if __name__ == '__main__':
    result = solve_part2()
    print(f"Grand total: {result}")