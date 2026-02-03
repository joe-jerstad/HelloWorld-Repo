total = 0
user_num = int(input('Enter a number: '))

for i in range(1, user_num + 1):
    total += (i ** 2)

print(total)