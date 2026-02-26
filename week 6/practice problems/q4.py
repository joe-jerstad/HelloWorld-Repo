def output_odd(smaller_num, larger_num):
    odd_lyst = []
    for i in range(smaller_num, larger_num + 1):
        if i % 2 == 1:
            odd_lyst.append(i)
    return odd_lyst

print(output_odd(37,1050))