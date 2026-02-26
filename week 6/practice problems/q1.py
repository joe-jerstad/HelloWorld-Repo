def skip_letter(word):
    word = word.replace(' ', '')
    i = 0
    letters_lyst = []
    for letter in range(len(word)):
        if i % 2 == 0:
            letters_lyst += word[i]
        i += 1
    return letters_lyst

print(skip_letter('banana sunday'))
