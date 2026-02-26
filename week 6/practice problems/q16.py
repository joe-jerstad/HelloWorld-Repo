def war_of_numbers(numbers):
    odds = 0
    evens = 0
    for num in numbers:
        if num % 2 == 0:
            evens += num
        else:
            odds += num
    
    if odds > evens:
        return 'odds'
    else:
        return 'evens'
    
print(war_of_numbers([2, 8, 7, 5]))

print(war_of_numbers([2, 8, 7, 5]))