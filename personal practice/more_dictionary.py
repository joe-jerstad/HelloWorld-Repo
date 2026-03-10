test_d = {'Emma' : 73, 'Jack' : 42, 'Ally' : 35, 'James' : 78}


def find_max(test):

    cur_max = -1

    for name in test:
        if test[name] > cur_max:
            cur_max = test[name]
            name_max = name 

    return name_max

print(find_max(test_d))

print(test_d['Emma'])

#caching values, aka storing values once instead of calculating multiple times increases memory complexity but lowers time complexity
#with many users increasing time taken can be more beneficial than increasing the memory used