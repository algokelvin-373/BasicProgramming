from collections import Counter


def find_modus_data_collection(numbers):
    if not numbers:     # if numbers is None
        return -1
    counts = Counter(numbers)
    max_count = max(counts.values())
    modus = [num for num, cnt in counts.items() if cnt == max_count]
    return modus[0]


result1 = find_modus_data_collection([1, 2, 2, 3, 3, 3])
result2 = find_modus_data_collection([4, 5, 6, 5, 4, 4, 5, 4, 4, 6])
print(f'Modus for Result1: {result1}')
print(f'Modus for Result2: {result2}')