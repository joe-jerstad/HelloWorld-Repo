def is_isogram(word):
    flag = True
    letter_list = []
    for letter in word:
        if letter not in letter_list:
            letter_list.append(letter)
        else:
            flag = False
    return flag

print(is_isogram('password'))

