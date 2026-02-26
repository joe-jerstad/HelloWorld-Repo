#part A:

receipt = {}

receipt['side salad'] = 6
receipt['chicken parm'] = 12
receipt['cookie'] = 3

#Part B:
total = 0
for item in receipt:
    total += receipt[item]

print(total)

