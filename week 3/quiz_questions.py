'''

1 a)
5
3
8
12

1 b)
my_var: 1 , 5 -> infinity (only odd)
my_var: 3
my_var: 2 - 10 (only even)
my_var: 12 -> infinity (only even)

2)
In code set a, the code will check if Boolean_A is true and run that if it is and regardless of if Boolean_A is true or false, it will check if Boolean_B is true
and run the second line of code if it is.

In code set b, the code will check if Boolean_A is true and run that if it is, and if it is true it will not check Boolean_B. If Boolean_A is false, it will
check Boolean_B and run that block of code if it is true.

'''

#3)
'''
light_color = input('Enter the color of the light: ').lower()

if light_color == 'green':
    print('Go')
elif light_color == 'yellow':
    print('Yield')
elif light_color == 'red':
    print('Stop')
else:
    print('Invalid Entry.')
'''
#4)
'''
max_num = int(input('Enter a number: '))
num_b = int(input('Enter another number: '))
if num_b > max_num:
    max_num = num_b
num_c = int(input('Enter another number: '))
if num_c > max_num:
    max_num = num_c
print(f'The largest number is {max_num}.')
'''
#5)
'''
min_num = int(input('Enter a number: '))
num_b = int(input('Enter another number: '))
if num_b < min_num:
    min_num = num_b
num_c = int(input('Enter another number: '))
if num_c < min_num:
    min_num = num_c
print(f'The largest number is {min_num}.')
'''
#6)
'''
import random as rnd

ai_choice = rnd.choice(['heads','tails'])

guess = input('Guess heads or tails: ').lower()

if guess == ai_choice:
    print('Correct!')
elif guess != ai_choice:
    print('Incorrect :(')
'''
#7
'''
vowels = ['a','e','i','o','u',]

user_letter = input('Enter a letter: ').lower()
if user_letter in vowels:
    print('vowel')
else:
    print('consonant')
'''
#8
'''
user_choice = input('Pick a flavor: ').lower()

if user_choice == 'vanilla':
    print(f'Here is your {user_choice} ice cream!')
elif user_choice == 'chocolate':
    print(f'Here is your {user_choice} ice cream!')
elif user_choice == 'strawberry':
    print(f'Here is your {user_choice} ice cream!')
else:
    print(f"Sorry, we don't have {user_choice} ice cream." )
'''
#9

'''
name = input('Enter the name: ').lower()
if name == 'darth vader':
    print('Father')
elif name == 'leia':
    print('Sister')
elif name == 'han':
    print('Brother in Law')
elif name == 'r2d2':
    print('Droid')
else:
    print('Unknown')
'''
    
#10

'''
num_a = int(input('Enter a number: '))
num_b = int(input('Enter another number: '))
num_c = int(input('Enter another number: '))

max_num = num_a
if num_b > max_num:
    max_num = num_b
if  num_c > max_num:
    max_num = num_c

min_num = num_a
if num_b < min_num:
    min_num = num_b
if  num_c < min_num:
    min_num = num_c

if (num_a <= num_b and num_a >= num_c) or (num_a <= num_c and num_a >= num_b):
    middle_num = num_a
elif (num_b <= num_a and num_b >= num_c) or (num_b <= num_c and num_b >= num_a):
    middle_num = num_b
elif (num_c <= num_a and num_c >= num_b) or (num_c <= num_b and num_c >= num_a):
    middle_num = num_c

print(f'{min_num} {middle_num} {max_num}')
'''

#11

'''
num_a = int(input('Enter a number: '))
num_b = int(input('Enter another number: '))
num_c = int(input('Enter another number: '))

max_num = num_a
if num_b > max_num:
    max_num = num_b
if  num_c > max_num:
    max_num = num_c

min_num = num_a
if num_b < min_num:
    min_num = num_b
if  num_c < min_num:
    min_num = num_c

if (num_a <= num_b and num_a >= num_c) or (num_a <= num_c and num_a >= num_b):
    middle_num = num_a
elif (num_b <= num_a and num_b >= num_c) or (num_b <= num_c and num_b >= num_a):
    middle_num = num_b
elif (num_c <= num_a and num_c >= num_b) or (num_c <= num_b and num_c >= num_a):
    middle_num = num_c

print(f'{max_num} {middle_num} {min_num}')
'''

#12


knuts = int(input('Enter amount of knuts: '))

currency_list = []

galleons = knuts // 493
sickles = (knuts % 493) // 29
remain_knuts = ((knuts % 493) % 29) 

if galleons > 0:
    if galleons == 1:
        currency_list.append(f'{galleons} galleon')
    else:
        currency_list.append(f'{galleons} galleons')
if sickles > 0:
    if sickles == 1:
        currency_list.append(f'{sickles} sickle')
    else:
        currency_list.append(f'{sickles} sickles')
if remain_knuts > 0:
    if remain_knuts == 1:
        currency_list.append(f'{remain_knuts} knut')
    else:
        currency_list.append(f'{remain_knuts} knuts')

for item in currency_list:
    print(f'{item}', end = ' ')

    
#13

'''
num_a = int(input('Enter a number: '))
num_b = int(input('Enter another number: '))
num_c = int(input('Enter another number: '))
repeat = 0

if num_a == num_b:
    repeat += 1
if num_a == num_c:
    repeat += 1
if num_b == num_c:
    repeat += 1

if repeat == 1:
    print('You repeated the same number twice')
elif repeat == 0:
    print('These are all unique numbers')
elif repeat == 3:
    print('These are all the same number')
'''
    
#14

'''
highway_num = int(input('Enter the highway number: '))
if highway_num % 100 == 0 or highway_num == 0 or highway_num > 1000:
    print('Invalid highway number')
elif highway_num % 2 == 1:
    print(f'Highway {highway_num} runs North/South')
elif highway_num % 2 == 0:
    print(f'Highway {highway_num} runs East/West')
'''

#15

'''
p1_wins = [('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')]

p1_pick = input('Player 1 choice: ').lower()
p2_pick = input('Player 2 choice: ').lower()

if (p1_pick, p2_pick) in p1_wins:
    print('Player 1 wins!')
else:
    print('Player 2 wins!')
'''
    
#16

'''
side_1 = input('Enter side length 1: ')
side_2 = input('Enter side length 2: ')
side_3 = input('Enter side length 3: ')

if side_1 == side_2 == side_3:
    print('equilateral triangle')
elif side_1 != side_2 and side_1 != side_3 and side_2 != side_3:
    print('scalene triangle')
else:
    print('isosceles triangle')
'''
    
#17 

'''
heart_rates = {
    'age 1' : {'above average' : '47-72', 'below average' : '73-93'},
    'age 2' : {'above average' : '46-71', 'below average' : '72-94'},
    'age 3' : {'above average' : '45-70', 'below average' : '71-97'},
}

age = int(input('Enter your age: '))
athleticism_goal = (input('Enter your athleticism goal: ')).lower()
if age >= 20 and age <= 39:
    age_group = 'age 1'
elif age >= 40 and age <= 59:
    age_group = 'age 2'
elif age >= 60 and age <= 79:
    age_group = 'age 3'


print(f'Your resting heart rate should be between {heart_rates[age_group][athleticism_goal]}')
'''

#18

'''
race = input('Enter the race: ')
the_class = input('Enter the class: ')

classes = {
    'warrior' : {'elf' : 150, 'ogre' : 200},
    'bard' : {'elf' : 75, 'ogre' : 100},
    'wizard' : {'elf' : 25, 'ogre' : 50}
}

health_points = (classes[the_class][race])

print(health_points)
'''

#19

'''
group_one = ['k', '1', '2', '3']
group_two = ['4', '5', '6', '7', '8']
group_three = ['9', '10', '11', '12']

time = {
    'group_one' : {'morning' : '9 AM', 'afternoon' : '1 PM'},
    'group_two' : {'morning' : '10 AM', 'afternoon' : '2 PM'},
    'group_three' : {'morning' : '11 AM', 'afternoon' : '3 PM'},
}

user_grade = input('Enter your grade: ').lower()
if user_grade in group_one:
    answer = 'group_one'
elif user_grade in group_two:
    answer = 'group_two'
elif user_grade in group_three:
    answer = 'group_three'
am_or_pm = input('Enter morning or afternoon: ').lower()

print(f'The pool is open at {time[answer][am_or_pm]}')

'''

