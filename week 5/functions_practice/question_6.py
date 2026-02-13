from random import randint

def odd_or_even(guess):
    ai_num = randint(0,9)
    if ai_num % 2 == 0:
        ai_num = 'even'
    else:
        ai_num = 'odd'
    if guess == ai_num:
        return 'Correct'
    else:
        return 'Incorrect'

print(odd_or_even('odd'))