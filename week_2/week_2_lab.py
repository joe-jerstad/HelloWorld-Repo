def convert_to_date(total_days):
    age_years = total_days // 360
    age_months = (total_days % 360) // 30
    age_days = round(((total_days % 360) % 30), 0)  
    return [age_years,age_months,age_days]

def main():
    human_age = float(input('Enter the human age: '))
    dog_age = (human_age * 7) * 360
    cat_age = (human_age / 9) * 360
    horse_age = 3 * (((((human_age ** 2) - 47) / 7) + 12)) * 360
    dog_age_list = convert_to_date(dog_age)
    cat_age_list = convert_to_date(cat_age)
    horse_age_list = convert_to_date(horse_age)
    print(f'Your age in dog years is {dog_age_list[0]} years {dog_age_list[1]} months {dog_age_list[2]} days.')
    print(f'Your age in cat years is {cat_age_list[0]} years {cat_age_list[1]} months {cat_age_list[2]} days.')
    print(f'Your age in cat years is {horse_age_list[0]} years {horse_age_list[1]} months {horse_age_list[2]} days.')

if __name__ == '__main__':
    main()

'''

#PART 1
#a)

human_age = float(input('Enter the human age: '))
dog_age = human_age * 7
cat_age = human_age / 9

print(f'Your age in dog years is: {round(dog_age, 1)}')
print(f'Your age in cat years is: {round(cat_age, 1)}')

#b)

human_age = float(input('Enter the human age: '))
dog_age_total_days = human_age * 7 * 360
dog_age_years = dog_age_total_days // 360
dog_age_months = (dog_age_total_days % 360) // 30
dog_age_days = round(((dog_age_total_days % 360) % 30),0)

print(f'Your dog years is {dog_age_years} years, {dog_age_months} months, and {dog_age_days} days.')

#PART 2
#a)

def convert_to_date(total_days):
    age_years = total_days // 360
    age_months = (total_days % 360) // 30
    age_days = round(((total_days % 360) % 30),0)
    return [age_years , age_months , age_days]

'''