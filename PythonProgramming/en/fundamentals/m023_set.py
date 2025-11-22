# Set can avoid duplicate data

set1 = {1, 2, 3, 2, 4, 6, 5, 1, 4, 6}
set2 = {3, 5, 5, 4, 4, 8, 7, 10, 9, 9}

print(f'set1 : {set1}')
print(f'set2 : {set2}')

print()

print(f'length set1 : {len(set1)}')
print(f'length set2 : {len(set2)}')

print()

print(f'Intersection set1 && set2 : {set1.intersection(set2)}')
print(f'Union set1 && set2        : {set1.union(set2)}')
