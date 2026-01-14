def count_frequency(items):
    freq = {}
    for item in items:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq


def get_unique_items(items):
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique


def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = value
    return result
print(count_frequency([1, 2, 2, 3]))
