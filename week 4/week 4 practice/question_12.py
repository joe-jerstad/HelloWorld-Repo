columns = int(input('Enter an integer: '))
rows = int(input('Enter another integer: '))
print('Your multiplication table: ')

for number in range(1, columns + 1):
    for other_number in range(1, rows + 1):
        print(f'{other_number * number:<4}', end = '')
    print()

