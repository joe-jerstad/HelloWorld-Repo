def add_lists(lyst1, lyst2):
    new_lyst = []
    for i in range(len(lyst1)):
        new_lyst.append(lyst1[i] + lyst2[i])

    return new_lyst

print(add_lists([1,2], [-1,1]))