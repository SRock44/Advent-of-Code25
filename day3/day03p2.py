def find_max_joltage_part2(bank, k=12):
    """
    find the maximum k-digit number by selecting exactly k batteries.
    uses greedy approach to select lexicographically largest subsequence.
    """
    digits = list(bank)
    n = len(digits)
    result = []
    start = 0
    
    for pos in range(k):
        # we need to pick (k - pos) more digits
        # we can look ahead up to position (n - (k - pos))
        remaining = k - pos
        max_end = n - remaining + 1
        
        # find the maximum digit in the valid range
        max_digit = max(digits[start:max_end])
        
        # find the first occurrence of this max digit
        for i in range(start, max_end):
            if digits[i] == max_digit:
                result.append(max_digit)
                start = i + 1
                break
    
    return int(''.join(result))

def solve_part2():
    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')
    
    total_joltage = 0
    
    for bank in lines:
        if not bank:
            continue
        max_jolt = find_max_joltage_part2(bank, 12)
        total_joltage += max_jolt
    
    return total_joltage

if __name__ == '__main__':
    result = solve_part2()
    print(f"Total output joltage (Part 2): {result}")