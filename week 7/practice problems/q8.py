def find_unique(numbers):
    number_dict = {}
    sol_lyst = []

    for num in numbers:
        if num not in number_dict:
            number_dict[num] = 1
        else:
            number_dict[num] += 1

    for i in number_dict:
        if number_dict[i] == 1:
            sol_lyst.append(i)
    
    return sol_lyst
        
test_1 = [1,9,8,8,7,6,1,6]
test_2 = [5,5,2,4,4,4,9,9,9,1]
test_3 = [9,5,6,8,7,7,1,1,1,1,1,9,8]

print(find_unique(test_1))