def is_two_digit_number(num):
    return 10 <= abs(num) <= 99

def report_two_digit_numbers(num_list):
    two_digits = []

    for num in num_list:
        if is_two_digit_number(num):
            two_digits.append(num)

    return two_digits

print(report_two_digit_numbers([100,57,12,1]))

print(report_two_digit_numbers([121,36,-19,-6,0,21]))

print(report_two_digit_numbers([100,7, 8437]))

