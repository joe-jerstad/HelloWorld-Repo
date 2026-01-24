'''

boolean(True or False)

== , equal , 3 == 4 (false)

!= , not equal, 3 != 4 (true)

< , less than

> , greater than

<= , less than or equal

>= , greater than or equal

Booleans have operators:
    or, and, not, etc.

TTF
TFF
TFT
FFT

Selection statements:
if
if - else
if - elif - else
False ----- Condition ----- True
 |                           |
 |                           |
block of code            block of code

if <condition>:
    <block of code>
else:
    <block of code>


'''

x = 3
y = 4

print(x == y)

user_age = int(input('What is your age?: '))

#correct
if user_age < 3:
    ticket_price = 0
elif user_age < 18:
    ticket_price = 10
elif user_age >= 65:
    ticket_price = 15
else:
    ticket_price = 20

#nested conditionals (works but elifs better)
'''
if user_age < 3:
    ticket_price = 0
else:
    if user_age < 18:
        ticket_price = 10
    else:
        if user_age >= 65:
            ticket_price = 15
        else:
            ticket_price = 20
'''
            
'''
military_service = input('Are you a member of the military? (y/n): ')

if military_service == 'y':
    ticket_price -= 5
'''
    
print(f'Your ticket price is ${ticket_price}.')