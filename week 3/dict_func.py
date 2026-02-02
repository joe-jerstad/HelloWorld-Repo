def find_oldest(name_dict):
    return max(name_dict, key=name_dict.get)
print(find_oldest({'Jack' : 45, 'Emma' : 72, 'Joe' : 41})) 