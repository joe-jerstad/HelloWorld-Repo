done = False
total = 0

while not done:
    user_int = int(input('Enter an integer: '))
    if user_int >= 0:
        total += user_int
    else:
        done = True

print(total)
    