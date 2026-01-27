
#num_units = int(input('How many units were purchased?: '))

max_num_of_units = -1
num_units = 1
budget = 1000

while num_units <= 10000:
    if num_units <= 100:
        price = 3.99
    elif num_units > 100 and num_units <=300:
        price = 2.99
    else:
        price = 1.99

    total_price = num_units * price

    if total_price <= budget and num_units > max_num_of_units:
        max_num_of_units = num_units

    num_units += 1

    #print(f'Price per unit = {price}')
    #print(f'The total price is: {total_price}')
    #print(f'The cost for {num_units} is {round(total_price,2)}')

print(f'The max units for ${budget} is {max_num_of_units}')







#print al of the numbers between 5 and 10

'''
num = 5

while num <= 1000000:
    if num % 2 == 0:
        print(num)
    num += 1
    
#orrrrr

the_num = 2
while the_num <= 1000000:
    print(the_num)
    the_num += 2
'''