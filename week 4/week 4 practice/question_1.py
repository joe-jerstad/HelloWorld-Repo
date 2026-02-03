larger = int(input('Enter the larger number: '))
smaller = int(input('Enter the smaller number: '))
total = 0

while larger > smaller:
    larger /= 2
    if larger > smaller:
        total += 1

print(total)

