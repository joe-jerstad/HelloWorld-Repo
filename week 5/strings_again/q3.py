def is_boiling(temp):
    if temp[-1] == 'C' and float(temp[:-1]) < 100:
        return False
    elif temp[-1] == 'F' and float(temp[:-1]) < 212:
        return False
    else:
        return True

print(is_boiling('0F'))

