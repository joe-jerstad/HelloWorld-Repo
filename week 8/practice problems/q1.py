from random import randint

def toss_coin(guess=0):
    value = randint(0, 1)

    if value == guess:
        return 'Correct!'
    else: 
        return 'Incorrect!'
        
print(toss_coin())
print(toss_coin(0))
print(toss_coin(1))

        
    
