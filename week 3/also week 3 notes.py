
#num_units = int(input('How many units were purchased?: '))
'''
max_num_of_units = -1
num_units = 1
budget = 1000

while num_units <= 10000:
    if num_units <= 100:
        price = 3.99
    elif num_units > 100 and num_units <=300:
        price = 2.99
    else:
        price = 1.99

    total_price = num_units * price

    if total_price <= budget and num_units > max_num_of_units:
        max_num_of_units = num_units

    num_units += 1

    #print(f'Price per unit = {price}')
    #print(f'The total price is: {total_price}')
    #print(f'The cost for {num_units} is {round(total_price,2)}')

print(f'The max units for ${budget} is {max_num_of_units}')






'''
#print al of the numbers between 5 and 10

'''
num = 5

while num <= 100:
    if num % 2 == 0:
        print(num)
    num += 1
    
#orrrrr

the_num = 2
while the_num <= 100:
    print(the_num)
    the_num += 2
'''

'''
x = 4
x = x + 1 #same as x += 1

x = x * 2 #same as x *= 2
'''

#add all odd numbers between 5 and 100 inclusively

'''
total = 0
num = 8


while num < 50:
    if num % 2 == 1:
        total += num
    num += 1


for number in range(6, 101, 2):
    total += number

print(f'total = {total}')
'''
'''
total = 0

for number in range(2, 7,):
    if number % 2 == 1:
        total += number
print(f'total = {total}')

#ask user for number until they type stop, once they do report the sum


total = 0
user_input = input('enter a number: ')
if user_input != 'stop':
    total += int(user_input)
'''


'''
for amount_of_time in range(0,1000):
    user_input = input('enter a number: ')
    if user_input != 'stop':
        user_number = int(user_input)
        total += user_number
'''
done = False
total = 0

while not done:
    user_input = input('Enter a number: ').lower()
    if user_input == 'stop':
        done = True
    else:
        total += int(user_input)

print(total)

#WHILE LOOPS PEAK FOR INDETERMINENT NUMBER OF OPERATIONS, FOR LOOPS NOT GOOD FOR THAT

#short-circuit evaluation
#if python can evaluate the value of a boolean expression before it evaluates all of its operands, it will

