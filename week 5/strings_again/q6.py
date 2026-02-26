def get_drink_ID(flavor, capacity):
    return flavor[0:3] + str(capacity)

print(get_drink_ID('apple', 500))