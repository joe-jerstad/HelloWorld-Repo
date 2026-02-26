def find_unique(numbers):
    number_dict = {}

    for num in numbers:
        if num not in number_dict:
            number_dict[num] = 1
        else:
            number_dict[num] += 1

    for i in number_dict:
        if number_dict[i] == 1:
            return i
        
test_1 = [1,2,2,3,3,4,4]
test_2 = [7,8,8,9,9,10,10]
test_3 = [5,6,6,7,7,8,8,5,9]

print(find_unique(test_3))