#class inheritence

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f'I am {self.name} and I am {self.age} years old')

    def speak(self):
        print('I dont know what I say')

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age) #reference the super class(Pet) and use that init to initialize name and age
        self.color = color
    
    def speak(self): #when you use create a method in an inherited class that is the same as inhereted class, it replaces
        #the inherited classes method
        print('Meow')

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old and I am {self.color}')

class Dog(Pet):
    def speak(self):
        print('Bark')

p = Pet('Tim', 34)
p.speak()
c = Cat('Bill', 12, 'Orange')
c.show()
d = Dog('Jill', 25)
d.speak()
