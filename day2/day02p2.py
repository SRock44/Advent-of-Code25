# day 2 part 2: Gift Shop - find invalid product IDs
# Invalid IDs are numbers made of a sequence of digits repeated at least twice
# Examples: 12341234 (1234 two times), 123123123 (123 three times), 
#           1212121212 (12 five times), 1111111 (1 seven times)

def is_invalid_id(num):
    """
    Check if a number is an invalid ID.
    An invalid ID is made of a sequence of digits repeated at least twice.
    """
    num_str = str(num)
    n = len(num_str)
    
    # Try different pattern lengths (must repeat at least twice)
    # Pattern length can be from 1 to n//2 (at least 2 repetitions)
    for pattern_len in range(1, n // 2 + 1):
        # Check if the number length is divisible by pattern length
        if n % pattern_len != 0:
            continue
        
        # Extract the pattern (first pattern_len digits)
        pattern = num_str[:pattern_len]
        
        # Check if the entire number is made of this pattern repeated
        num_repetitions = n // pattern_len
        expected = pattern * num_repetitions
        
        if num_str == expected:
            return True
    
    return False

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

