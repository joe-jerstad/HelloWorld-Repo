def output_even(smaller_num, larger_num):
    even_lyst = []
    for i in range(smaller_num, larger_num + 1):
        if i % 2 == 0:
            even_lyst.append(i)
    return even_lyst

print(output_even(37,1050))