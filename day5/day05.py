def parse_input(filename):
    """
    parse the input file into fresh ranges and available ingredient ids
    """
    with open(filename, 'r') as f:
        content = f.read().strip()
    
    # split by blank line
    parts = content.split('\n\n')
    ranges_section = parts[0]
    ingredients_section = parts[1]
    
    # parse the ranges
    ranges = []
    for line in ranges_section.split('\n'):
        if line:
            start, end = map(int, line.split('-'))
            ranges.append((start, end))
    
    # parse the ingredient ids
    ingredients = []
    for line in ingredients_section.split('\n'):
        if line:
            ingredients.append(int(line))
    
    return ranges, ingredients

def is_fresh(ingredient_id, ranges):
    """
    check if an ingredient id falls into any of the fresh ranges
    """
    for start, end in ranges:
        if start <= ingredient_id <= end:
            return True
    return False

def solve():
    ranges, ingredients = parse_input('input.txt')
    
    # count how many ingredients are fresh
    fresh_count = 0
    for ingredient_id in ingredients:
        if is_fresh(ingredient_id, ranges):
            fresh_count += 1
    
    return fresh_count

if __name__ == '__main__':
    result = solve()
    print(f"Fresh ingredients: {result}")