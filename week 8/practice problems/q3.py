def count_duplicates(num_1=0, num_2=0, num_3=0):
    if num_1 != num_2 and num_1 != num_3 and num_2 != num_3:
        return 'Each number is unique'
    elif num_1 == num_2 and num_1 == num_3:
        return 'There are 3 of the same number'
    else:
        return 'There are 2 of the same number'
    
print(count_duplicates(2,3,2))
print(count_duplicates(4,4,4))
print(count_duplicates(1,2,3))
print(count_duplicates(1))
print(count_duplicates(0))