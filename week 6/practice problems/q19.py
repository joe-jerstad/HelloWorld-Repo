def is_acronym(s, words):
    compare = ''

    for word in words:
        compare += word[0]
        
    return compare == s

print(is_acronym('ngguoy', ['never', 'gonna', 'give', 'up', 'on', 'you']))