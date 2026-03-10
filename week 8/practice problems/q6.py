def halistone_seq(n=40):
    hali = f'{n}'

    while n != 1:
        if n % 2 == 0:
            n /= 2
            hali += f', {int(n)}'
        else:
            n = (n * 3) + 1
            hali += f', {int(n)}'

    return hali

print(halistone_seq(25))
print(halistone_seq(40))
print(halistone_seq())

