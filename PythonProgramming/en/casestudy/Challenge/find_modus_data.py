from collections import Counter


def find_modus_data(numbers):
    modus_number = 0
    for num in set(numbers):
        if num == numbers.count(num) and num > modus_number:
            modus_number = num
    return modus_number

def find_modus_data_collection(numbers):
    return lambda nums: max(
        [num for num, cnt in Counter(nums).items() if num == cnt],
        default=-1
    )

result1 = find_modus_data([1, 2, 2, 3, 3, 3])
result2 = find_modus_data([4, 5, 6, 5, 4, 4, 5, 4, 4, 6])
print(f'Modus for Result1: {result1}')
print(f'Modus for Result2: {result2}')

result1 = find_modus_data_collection([1, 2, 2, 3, 3, 3])
result2 = find_modus_data_collection([4, 5, 6, 5, 4, 4, 5, 4, 4, 6])
print(f'Modus for Result1: {result1}')
print(f'Modus for Result2: {result2}')