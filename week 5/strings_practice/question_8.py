def last_letters(sentence):
    new_word = ''
    word_list = sentence.split()
    for word in word_list:
        new_word += word[-1]
    return new_word

print(last_letters('the magic is within you'))