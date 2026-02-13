from random import randint

value = randint(0,1)

def heads_or_tails(user_guess):
    value = randint(0,1)
    if user_guess == value:
        return 'Correct'
    else:
        return 'Incorrect'

print(heads_or_tails(0))