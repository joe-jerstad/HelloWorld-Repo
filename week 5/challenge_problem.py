'''
JUST NEED TO ADD ALL THE LETTERS BUT NOT FUN SOLUTION
def decode_word(sentence):
    new_string = ''
    for letter in sentence:
        if letter not in ['L','T','3','Q','A','V']:
            new_string += letter
        elif letter == 'L':
            new_string += 
'''

letter_decode = {
    'L' : 'T',
    'T' : 'L',
    '3' : 'A',
    'Q' : 'A',
    'A' : 'E',
    'V' : 'B'
}

def decode_word(sentence):
    new_string = ''
    for letter in sentence:
        if letter not in letter_decode.keys():
            new_string += letter
        else:
            new_string += letter_decode[letter]
    return new_string

print(decode_word('3TRAQDY T3LA'))


'''
def decode_uu(sentence):
    sentence += ' '
    new_string = ''
    for index in range(0, len(sentence)-1):
        if sentence[index] == 'U' and sentence[index + 1] == 'U':
            new_string += 'W'

        elif sentence[index] == 'U' and sentence[index - 1] == 'U':
            pass
        else:
            new_string += sentence[index]
    return new_string

print(decode_uu('EOUUUUOUU'))
'''

#SOOOO LOCKED IN 2 POINTER
def decode_uu(sentence):
    sentence += ' '
    i = 0
    new_string = ''
    while i < len(sentence):
        if sentence[i] == 'U' and sentence[i + 1] == 'U':
            new_string += 'W'
            i += 2
        else:
            new_string += sentence[i]
            i += 1
    return new_string

print(decode_uu('EOUUUUOUU'))
        
