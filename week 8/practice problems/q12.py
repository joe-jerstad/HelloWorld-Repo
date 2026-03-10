def is_even(num):
    return num % 2 == 0

def report_evens(num_list):
    evens = []

    for num in num_list:
        if is_even(num):
            evens.append(num)

    return evens

print(report_evens([4, 3, 12, 16, 8, 9, 25]))
print(report_evens([6, 100, 3, 12, 16, 6, 9, 100]))
print(report_evens([3, 99, 7, 13, 25]))