def reverse_string(word):
    word_reversed = ''
    index = len(word) - 1
    for i in range(len(word)):
        word_reversed += word[index]
        index -= 1
    return word_reversed

print(reverse_string('hello'))
