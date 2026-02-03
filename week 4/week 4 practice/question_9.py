n = 25

while n != 1:
    print(int(n))
    if n % 2 == 0:
        n /= 2
    else:
        n = (n * 3) + 1

print(int(n))