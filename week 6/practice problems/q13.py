def get_indices(lyst, item):
    index_lyst = []
    for i in range(len(lyst)):
        if lyst[i] == item:
            index_lyst.append(i)

    return index_lyst

print(get_indices(['a','a','b','a','b','a'], 'a'))