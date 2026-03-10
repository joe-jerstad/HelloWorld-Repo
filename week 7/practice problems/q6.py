def is_isogram(word):
    seen = {}

    for letter in word:
        if letter in seen:
            return False
        else:
            seen[letter] = 1
    return True

test_1 = 'algorism'
test_2 = 'password'
test_3 = 'consecutive'

print(is_isogram(test_1))
print(is_isogram(test_2))
print(is_isogram(test_3))
