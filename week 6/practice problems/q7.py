#come back too much work

def ascending_order(num_a, num_b, num_c):

    max_num = num_a
    if num_b > max_num:
        max_num = num_b
    if  num_c > max_num:
        max_num = num_c

    min_num = num_a
    if num_b < min_num:
        min_num = num_b
    if  num_c < min_num:
        min_num = num_c

    if (num_a <= num_b and num_a >= num_c) or (num_a <= num_c and num_a >= num_b):
        middle_num = num_a
    elif (num_b <= num_a and num_b >= num_c) or (num_b <= num_c and num_b >= num_a):
        middle_num = num_b
    elif (num_c <= num_a and num_c >= num_b) or (num_c <= num_b and num_c >= num_a):
        middle_num = num_c

    return [min_num, middle_num, max_num]

print(ascending_order(2,45,4))