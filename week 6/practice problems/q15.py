def count(cards):
    op_1 = [2, 3, 4, 5, 6]
    op_2 = [10, 'j', 'q', 'k', 'a']
    total = 0

    for i in cards:
        if i in op_1:
            total += 1
        elif i in op_2:
            total -= 1
    
    return total

print(count(['a', 'a', 'k', 'q', 'q', 'j']))