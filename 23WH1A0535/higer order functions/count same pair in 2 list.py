def count_same_pairs(list1, list2):
    # Use map to create pairs from corresponding elements of both lists
    pairs = list(map(lambda x, y: (x, y), list1, list2))

    # Count occurrences of each pair
    pair_count = {}
    for pair in pairs:
        pair_count[pair] = pair_count.get(pair, 0) + 1

    return pair_count

# Example usage:
list1 = [1, 2, 3, 4]
list2 = [2, 1, 3, 4]

result = count_same_pairs(list1, list2)
print(result)
