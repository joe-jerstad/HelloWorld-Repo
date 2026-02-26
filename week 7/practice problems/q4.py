def find_youngest(people):
    cur_min = 500

    for person in people:
        if people[person] < cur_min:
            cur_min = people[person]
            name_min = person
        
    return name_min

test_1 = {'Emma' : 71, 'Jack' : 45, 'Olivia' : 82,'Liam': 39}
test_2 = {'Sophia' : 50, 'Mason' : 68, 'Ava' : 67, 'Noah' : 33}
test_3 = {'Ethan' : 25, 'Lucas' : 30, 'Mia' : 29}

print(find_youngest(test_1))
            
