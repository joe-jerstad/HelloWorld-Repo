grade = input('Enter your grade: ')
time = input('Enter morning or afternoon: ').lower()

if grade != 'k':
    grade = int(grade)

if grade == 'k' or grade >= 1 and grade <= 3:
    if time == 'morning':
        pool_time = '9 AM'
    elif time == 'afternoon':
        pool_time = '1 PM'
elif grade >= 4 and grade <= 8:
    if time == 'morning':
        pool_time = '10 AM'
    elif time == 'afternoon':
        pool_time = '2 PM'
elif grade >= 9 and grade <= 12:
    if time == 'morning':
        pool_time = '11 AM'
    elif time == 'afternoon':
        pool_time = '3 PM'

print(f'The pool is open at {pool_time}.') 