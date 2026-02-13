def flip_flop(word):
    middle = len(word) // 2
    
    if len(word) % 2 == 1: # odd
        return word[middle + 1:] + word[middle] + word[:middle]
    else:
        return word[middle:] + word[:middle]
print(flip_flop('grapes'))

    