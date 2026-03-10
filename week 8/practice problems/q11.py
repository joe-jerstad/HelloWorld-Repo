def multiples(num, length=5):
    multiples = []

    for i in range(1, length + 1):
        multiples.append(i * num)

    return multiples

print(multiples(7, 5))
print(multiples(12, 10))
print(multiples(2))
print(multiples(2, 3))

