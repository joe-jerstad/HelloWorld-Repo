height = int(input('Enter a height: '))

print(f'Here is a triangle of height {height}: ')
for i in range(1, height + 1):
    print('*' * i)