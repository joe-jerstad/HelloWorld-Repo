#object oriented programming'
'''
x = 1
print(type(x))

def hello(): 
    print('hello')

print(type(hello)) #type 'function' is an object


string = 'hello'
print(string.upper()) #.upper() is a method that is acting on an object, methods that you can do are based on the type of object that 
#they are, ex cant do .upper() on an int

'''

class Dog: #use camel case for classes

    def __init__(self, name, age):
        self.name = name #attribute of class dog which is name
        self.age = age
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age
        

    '''
    def add_one(self, x):
        return x + 1

    def bark(self): #method, function that goes inside of a class, all methods have parameter self
        print('bark')
    '''

'''
d = Dog('Tim', 34) #d is an object of type Dog
d.set_age(23)
print(d.get_age())


d2 = Dog('Bill', 12)
print(d2.get_age())

d.bark() #call the method on class Dog object using a method that is defined
print(type(d))
print(d.add_one(5))
'''


