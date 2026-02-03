user_word = input('Enter your word: ')

for letter in user_word[1::2]:
    print(letter, end = '')