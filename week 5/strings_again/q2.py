def is_fever(temp):
    if temp[-1] == 'C' and float(temp[:-1]) <= 37:
        return False
    elif temp[-1] == 'F' and float(temp[:-1]) <= 98.6:
        return False
    else:
        return True

print(is_fever('98F'))

