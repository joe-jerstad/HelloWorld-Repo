#idk if this meets the parameters

def reverse_string(word):
    index = len(word) - 1
    new_word = ''
    for i in range(len(word)):
        new_word += word[index]
        index -= 1
    return(new_word)

print(reverse_string('hello'))