def is_isogram(word):
    seen = ''
    for l in word:
        if l in seen:
            return False
        seen += l
    return True

print(is_isogram('python'))