#maybe try to do with proper two pointer logic that doesnt use the space adding and handle the last letter seperately
#your methods are NOT good practice

def last_letters(sentence):
    words = sentence.split()
    lasts = ''
    
    for word in words:
        lasts += word[-1]
    
    return lasts

print(last_letters('the magic is within you'))

def new_last_letters(sentence):

    lasts = ''

    for i in range(len(sentence) - 1):
        if sentence[i + 1] == ' ':
            lasts += sentence[i]

    lasts += sentence[-1]
    
    return lasts

print(new_last_letters('the magic is within you'))

