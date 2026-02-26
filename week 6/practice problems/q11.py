def largest_odd(numbers):
    largest = -1

    for num in numbers:
        if num % 2 == 1 and num > largest:
            largest = num

    return largest


print(largest_odd([3,7,2,1,7,9,10,13]))