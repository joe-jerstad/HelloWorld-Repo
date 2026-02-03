width = int(input('Enter the width: '))
length = int(input('Enter the length: '))
pattern = input('Enter the pattern: ')

for i in range(length):
    print(f'{width * pattern}')