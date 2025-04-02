print(f'Range function {range(1, 10)}')

print('Range 1')
for number in range(1, 10):
    print(number)

print('Range 2: with 2 Step')
for number in range(1, 10, 2):
    print(number)

print('Logic SUM data')
total = 0
for number in range(1, 10):
    total += number
print(f"Total: {total}")