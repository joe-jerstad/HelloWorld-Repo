def letter_count(word):
    seen = {}

    for letter in word:
        if letter in seen:
            seen[letter] += 1
        else:
            seen[letter] = 1
        
    return seen

test_1 = 'hello'
test_2 = 'mississippi'
test_3 = 'apple'

print(letter_count(test_2))
