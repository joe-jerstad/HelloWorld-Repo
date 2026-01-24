import math

#question 1

chickens = int(input('How many chickens do you have?: '))
cows = int(input('How many cows do you have?: '))
pigs = int(input('How many pigs do you have?: '))
total_legs = (chickens * 2) + (cows * 4) + (pigs * 4)

print(f'The total amount of legs on your farm is {total_legs}.')

#question 2

two_pointers = int(input('How many 2 pointers did your team score?: '))
three_pointers = int(input('How many 3 pointers did your team score?: '))

print(f'Your team scored {(three_pointers * 3) + (two_pointers * 2)}.')

#question 3

top_base = int(input('What is the top base of your trapezoid?: '))
bottom_base = int(input('What is the bottom base of your trapezoid?: '))
height = int(input('What is the height of your trapezoid?: '))
area_of_trapezoid = ((top_base + bottom_base) / 2) * height

print(f'The area of your trapezoid is {area_of_trapezoid}.')

#question 4

base_edge = int(input('Enter the base edge of your pyramid: '))
height = int(input('Enter the height of your pyramid: '))
volume = ((base_edge ** 2) * height) / 3

print(f'The volume of your right square pyramid is {round(volume, 1)}.')

#question 5

height = int(input('Enter the height of your cylinder: '))
radius = int(input('Enter the radius of your cylinder: '))
volume = math.pi * (radius ** 2) * height

print(f'The volume of your cylinder is {round(volume, 1)}.')

#question 6

radius = int(input('Enter the radius of your sphere: '))
volume = (4 / 3) * math.pi * (radius ** 3)

print(f'The volume of your sphere is {round(volume, 1)}.')

#question 7

radius = int(input('Enter the radius of your cone: '))
height = int(input('Enter the height of your cone: '))
volume = (((radius ** 2) * height) / 3) * math.pi

print(f'The volume of your cone is {round(volume, 2)}.')

#question 8 

radius = int(input('Enter the radius of your semi-circle: '))
area = (1 / 2) * math.pi * (radius ** 2)

print(f'The area of your semi-circle is {round(area, 1)}.')
