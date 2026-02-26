def list_of_multiples(num, length):
    multi_lyst = []

    for i in range(1, length + 1):
        multi_lyst.append(i * num)
    
    return multi_lyst

print(list_of_multiples(12, 10))
