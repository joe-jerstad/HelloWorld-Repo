#PART 1
#a)

human_age = float(input('Enter the human age: '))
dog_age = human_age * 7

print(round(dog_age, 1))

#b)

human_age = float(input('Enter the human age: '))
dog_age_total_days = human_age * 7 * 365
dog_age_years = dog_age_total_days // 365
dog_age_months = (dog_age_total_days % 365) // 30
dog_age_days = (int((dog_age_total_days % 365) % 30))   

print(f'Your dog years is {dog_age_years} years, {dog_age_months} months, and {dog_age_days} days.')
