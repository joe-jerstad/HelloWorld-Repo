from random import randint

def guess(guess='even'):
    value = randint(0,9)

    if value % 2 == 0:
        x = 'even'
    else:
        x = 'odd'

    if x == guess:
        return 'Correct!'
    else:
        return 'Incorrect!'
    
print(guess())
print(guess('even'))
print(guess('odd'))


