
upper_bound = int(input('Enter an upper bound for a check: '))

perfect = 0
abundant = 0
deficient = 0

for number in range(1, upper_bound + 1):   
    total = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            total += divisor
    if total == number:
        perfect += 1
    elif total < number:
        deficient += 1
    elif total > number:
        abundant += 1

print(f'Between 1 and 20 \n {deficient} deficient numbers \n {perfect} perfect numbers \n {abundant} abundant numbers.')


            
    
    


