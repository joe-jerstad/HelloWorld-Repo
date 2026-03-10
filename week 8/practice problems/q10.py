def find_factors(num=36):
    factors = ''

    for number in range(1, num):
        if num % number == 0:
            factors += f'{number}, '
    
    factors += f'{num}'

    return factors

print(find_factors(12))
print(find_factors(17))
print(find_factors(36))
print(find_factors())
