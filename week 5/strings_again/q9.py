def flip_flop(word):
    mid_point = len(word) // 2
    if len(word) % 2 == 0:
        return word[mid_point:] + word[:mid_point]
    elif len(word) % 2 == 1:
        return word[mid_point + 1:] + word[mid_point] + word[:mid_point]
    
print(flip_flop('abcd'))
print(flip_flop('grapes'))
print(flip_flop('abcde'))
print(flip_flop('cranberries'))
