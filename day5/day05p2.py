def parse_ranges(filename):
    """
    parse just the ranges section from the input file
    """
    with open(filename, 'r') as f:
        content = f.read().strip()
    
    # split by blank line and take the first part
    ranges_section = content.split('\n\n')[0]
    
    # parse the ranges
    ranges = []
    for line in ranges_section.split('\n'):
        if line:
            start, end = map(int, line.split('-'))
            ranges.append((start, end))
    
    return ranges

def merge_ranges(ranges):
    """
    merge overlapping ranges to count total unique ids
    """
    if not ranges:
        return []
    
    # sort ranges by start position
    sorted_ranges = sorted(ranges)
    
    # merge overlapping or adjacent ranges
    merged = [sorted_ranges[0]]
    
    for start, end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]
        
        # if current range overlaps or is adjacent to last range, merge them
        if start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, end))
        else:
            # no overlap, add as new range
            merged.append((start, end))
    
    return merged

def count_fresh_ids(ranges):
    """
    count total number of fresh ingredient ids across all ranges
    """
    merged = merge_ranges(ranges)
    
    total = 0
    for start, end in merged:
        # inclusive range, so add 1
        total += (end - start + 1)
    
    return total

def solve_part2():
    ranges = parse_ranges('input.txt')
    return count_fresh_ids(ranges)

if __name__ == '__main__':
    result = solve_part2()
    print(f"Total fresh ingredient IDs: {result}")