# day 3: Escalator Power - find maximum joltage from each bank
# each bank has batteries labeled 1-9
# need to turn on exactly 2 batteries
# joltage = number formed by the two digits (in order)

def find_max_joltage(bank):
    """
    Find the maximum joltage possible from a bank by selecting exactly 2 batteries.
    Returns the maximum two-digit number that can be formed.
    """
    digits = list(bank)
    n = len(digits)
    max_joltage = 0
    
    # try all pairs of positions (i, j) where i < j
    for i in range(n):
        for j in range(i + 1, n):
            # form the number from digits[i] and digits[j]
            joltage = int(digits[i] + digits[j])
            max_joltage = max(max_joltage, joltage)
    
    return max_joltage

def solve():
    # read input
    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')
    
    total_joltage = 0
    
    # process each bank
    for bank in lines:
        if not bank:
            continue
        max_jolt = find_max_joltage(bank)
        total_joltage += max_jolt
    
    return total_joltage

if __name__ == '__main__':
    result = solve()
    print(f"Total output joltage: {result}")

