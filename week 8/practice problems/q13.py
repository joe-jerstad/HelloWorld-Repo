def is_vowel(letter):
    return letter in 'aeiou'
    
def return_vowels(word):
    vowels = []

    for letter in word:
        if is_vowel(letter):
            vowels.append(letter)
    
    return vowels

print(return_vowels('apple'))
print(return_vowels('banana'))
print(return_vowels('run time error'))

