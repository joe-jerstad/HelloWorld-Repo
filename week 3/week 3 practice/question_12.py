#galleons = 29(knuts in 1 sickle) * 17(sickles in one galleon) 
#sickles = 29 knuts
#only print nonzero

knuts = int(input('Enter amount of knuts: '))

galleons = knuts // 493
sickles = (knuts % 493) // 29
remaining_knuts = (knuts % 493) % 29

if galleons > 0:
    print(f'{galleons} galleons', end = ' ')
if sickles > 0:
    print(f'{sickles} sickles', end = ' ')
if remaining_knuts > 0:
    print(f'{remaining_knuts} knuts', end = ' ')