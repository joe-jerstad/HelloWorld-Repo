def get_drink_ID(fruit, capacity):
    return fruit[0:3] + str(capacity)

print(get_drink_ID('watermelon', 750))