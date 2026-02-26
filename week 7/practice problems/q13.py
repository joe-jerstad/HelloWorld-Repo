calories = {'apple' : 95, 'banana' : 105, 'orange' : 62, 'grape' : 3, 'pear' : 102}

def total_calories(fruits):
    total = 0

    for fruit in fruits:
        if fruit in calories:
            total += calories[fruit]

    return total

test_1 = ['apple', 'banana', 'orange']
test_2 = ['grape', 'grape', 'grape', 'grape', 'grape']

print(total_calories(test_2))

print(len(calories))
