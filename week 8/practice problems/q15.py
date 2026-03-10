def is_negative(num):
    return num < 0

def is_odd(num):
    return num % 2 == 1

def report_negative_odds(num_list):
    negative_odds = []

    for num in num_list:
        if is_odd(num):
            if is_negative(num):
                negative_odds.append(num)

    return negative_odds

print(report_negative_odds([100, -57, 12, 1, -36, -15]))
print(report_negative_odds([121, -101, 36, -19, -6, 0, 21, -1]))
print(report_negative_odds([-100, 7, 8437]))
