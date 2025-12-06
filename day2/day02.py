# day 2: Gift Shop - find invalid product IDs
# Invalid IDs are numbers made of a sequence of digits repeated twice
# Examples: 55 (5 twice), 6464 (64 twice), 123123 (123 twice)

def is_invalid_id(num):
    """
    Check if a number is an invalid ID.
    An invalid ID is made of a sequence of digits repeated twice.
    """
    num_str = str(num)
    # Must have even length to be made of two equal parts
    if len(num_str) % 2 != 0:
        return False
    
    # Split into two halves
    mid = len(num_str) // 2
    first_half = num_str[:mid]
    second_half = num_str[mid:]
    
    # Check if first half equals second half
    return first_half == second_half

def solve():
    # Read input
    with open('input.txt', 'r') as f:
        content = f.read().strip()
    
    # Parse ranges (comma-separated, each range is start-end)
    ranges = []
    for range_str in content.split(','):
        if not range_str:
            continue
        start, end = map(int, range_str.split('-'))
        ranges.append((start, end))
    
    # Find all invalid IDs in all ranges
    invalid_ids = []
    
    for start, end in ranges:
        for num in range(start, end + 1):
            if is_invalid_id(num):
                invalid_ids.append(num)
    
    # Sum all invalid IDs
    total = sum(invalid_ids)
    return total

if __name__ == '__main__':
    result = solve()
    print(f"Sum of invalid IDs: {result}")

