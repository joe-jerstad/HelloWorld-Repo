def greeting(name:str = 'unknown', age:int = 'unknown'): #put :str lets the user know it should be a string input(type hint shown when writing function)
    initial = f'hello {name}! '  

    if age == 'unknown':
        initial += 'How old are you?'
    else:
        initial += f'Its cool being {age} years old'

    print(initial)


'''
def greeting(name):
    print(f'hello {name}. How old are you?')
'''

'''
greeting('ashley', 35)

greeting('ashley')

greeting('dexter', 8)

greeting(name = 'cam', age = 3) #keyword arguments rather than positional arguments

greeting(age = 3, name = 'cam')

greeting(name = 'cam', age = 3)
'''

'''
personal research:
args*
kwargs**
'''

def fctn1(num):
    return num + 1

x = 3
y = fctn1(x)

print(x)
print(y)

def fctn2(lyst):
    lyst.append('a')


lyst1 = [1,2,3]

print(lyst1)
fctn2(lyst1)
print(lyst1)

lyst1 = [1,2,3]
lyst2 = lyst1 #lyst2 points to the same spot in memory as lyst1
lyst2.append(4) 

print(lyst1)

x = 3
y = x
y += 1 

print(x)