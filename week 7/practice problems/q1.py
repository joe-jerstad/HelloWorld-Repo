def find_oldest(people):
    cur_max = -1

    for person in people:
        if people[person] > cur_max:
            cur_max = people[person]
            name_max = person
        
    return name_max

test_1 = {'Emma' : 71, 'Jack' : 45, 'Olivia' : 82,'Liam': 39}
test_2 = {'Sophia' : 50, 'Mason' : 68, 'Ava' : 67, 'Noah' : 33}
test_3 = {'Ethan' : 25, 'Lucas' : 30, 'Mia' : 29}

print(find_oldest(test_3))
            
