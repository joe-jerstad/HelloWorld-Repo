def skip_letter(word):
    i = 0
    letters_lyst = []
    for letter in range(len(word)):
        if i % 2 == 1:
            letters_lyst += word[i]
        i += 1
    return letters_lyst

print(skip_letter('banana sunday'))

def skipped_letter(word):
    letters_lyst = []
    for letter in word[1::2]:
        letters_lyst.append(letter)
    return letters_lyst

print(skipped_letter('banana sunday'))