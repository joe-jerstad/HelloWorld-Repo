def get_names(names):
    name_list = []

    for id in names:
        name_list.append(names[id])
    
    return name_list

print(get_names({ "01475": "Steve", "87469": "Alice", "654123": "Bob" }))
print(get_names({ "ID1": "John", "ID2": "Emma", "ID3": "Liam" }))
print(get_names({}))
