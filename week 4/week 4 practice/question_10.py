largest_num = -1
user_num = 0

while user_num >= 0:
    user_num = int(input('Enter a number: '))
    if user_num % 2 == 0 and user_num > 0 and user_num > largest_num:
        largest_num = user_num
    
print(f'Largest = {largest_num}')