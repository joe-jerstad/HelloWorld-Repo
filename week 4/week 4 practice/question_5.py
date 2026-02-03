factor = int(input('Enter a number: '))

for i in range(1,factor + 1):
    if factor % i == 0:
        print(i, end = ' ')