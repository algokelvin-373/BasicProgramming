def factor_pair(data):
    for number in range(1, int(data**0.5) + 1):
        if data % number == 0:
            divided = int(data / number)
            print(f'({number}, {divided})')


data_number = 450
print(f'__{data_number}__')
print(factor_pair(data_number))