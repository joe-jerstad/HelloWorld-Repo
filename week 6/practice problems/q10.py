def largest_even(numbers):
    largest = -1

    for num in numbers:
        if num % 2 == 0 and num > largest:
            largest = num

    return largest


print(largest_even([3,7,2,1,7,9,10,13]))