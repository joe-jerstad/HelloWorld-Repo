#to initialize a dictionary in python we use {}

#my_dictionary = {} #this is an empty dictionary

#we can initialize a dictionary with initial values with the following code:
#the keys and values are seperated by a : and key-value pairs are seperated by ,

#phonebook = {'matt' : 1438, 'ashley' : 1234}

#print(phonebook)

#to add to a dictionary -> phonebook[key] = value

#phonebook['waters'] = 5678

#print(phonebook)

#print(phonebook['matt'])

#print(phonebook[0])

#print(phonebook['waters'])

#lyst = ['matt', 'ashley']

#print(lyst[0])

#print(phonebook)

#print(phonebook.keys()) #returns the keys as a list(not really a list)

'''
for key in phonebook.keys():
    value = phonebook[key]
    msg = (f'Name: {key}   Number: {value}')
    print(msg)
'''

#create an empty dictionary.
#add functionality to allow each person at your table to enter their name and age from the console
#store that information in a dictionary
#once the program gets an input of 'done' print each persons name and age on a single line


my_dict = {}

flag = True

while flag:
    i = input('Enter your name: ')

    if i != 'done':
        x = input('Enter your age: ')
        if x != 'done':
            my_dict[i] = x
        else:
            flag = False
    else:
        flag = False

for i in my_dict: #by default python iterates through the keys (dont need .keys())
    print(f'Name: {i} Age: {my_dict[i]}', end = '   ')

#dont iterate through the values, only iterate through the keys

