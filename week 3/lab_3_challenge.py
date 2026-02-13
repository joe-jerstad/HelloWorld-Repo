earned_income = int(input('Enter your amount of earned income for 2023: '))
print('Are you single or married?: ')
marital_status = input('Enter "s" for single or "m" for married: ')

if marital_status == 's':
    if earned_income >= 0 and earned_income <= 11000:
        tax = earned_income * .1
    elif earned_income >= 11001 and earned_income <= 44725:
        tax = earned_income * .12
    elif earned_income >= 44726 and earned_income <= 95375:
        tax = earned_income * .22
    elif earned_income > 95475:
        tax = 'too much'

elif marital_status == 'm':
    if earned_income >= 0 and earned_income <= 22000:
        tax = earned_income * .1
    elif earned_income >= 22001 and earned_income <= 89450:
        tax = earned_income * .12
    elif earned_income >= 89451 and earned_income <= 190750:
        tax = earned_income * .22
    elif earned_income > 190750:
        tax = 'too much'

if tax == 'too much':
    print('Congrats, you made too much for this calculator!')
else:
    print(f'This year you owe {tax} in taxes.')

