def is_fever(temp):
    if temp.lower()[-1] == 'c' and float(temp[0:-1]) > 37:
        return True
    elif temp.lower()[-1] == 'f' and float(temp[0:-1]) > 98.6:
        return True
    else:
        return False
    
print(is_fever('99F'))
