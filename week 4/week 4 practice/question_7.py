new_word = ''
done = False

while not done:
    letter = input('Enter a letter(or type done): ')
    if letter == 'done':
        done = True
    else:
        new_word += letter

print(new_word)