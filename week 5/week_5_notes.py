

#ask the user for two bounds and print each of the even numbers between those bounds (include the upper bound)

def even_printer():
    lower_bound = int(input('enter lower bound: '))
    upper_bound = int(input('enter upper bound: '))

    for num in range(lower_bound, upper_bound + 1):
        if num % 2 == 0:
            print(num)

#even_printer()

def greeting(name):
    print(f'Hello {name}. How are you? ')

#greeting('Nils')
#greeting('Ivan')

def add_three(number):
    number = number + 3
    return number
'''
x = 10
print(x)
x = add_three(x)
print(x)
'''

def max_of_3(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3

def x_in_word(word):
    '''this function will take a word 
    and determine if that word has an x in it'''
    for letter in word:
        if letter == 'x':
            return True
    return False

#print(x_in_word('wadwadawawdawd'))

#help(x_in_word)

#on quiz, do need end statement, do not need formatting

'''
for num1 in range(1,4):
    for num2 in range(1, 5):
        print(f'{num1 * num2 :3.0f}', end=' ')
    print()
'''

'''

collection types:
sequential and non-sequential
sequential:
-strings
-lists: put any type of information in the list, can be strings, floats, ints, booleans, etc
==to initialize a list use[]

'''

#answers = 'A C A A CA D B A'

lst = ['a', 'apple', 7, 17.1, True, 456]

#print(lst)
#lst.append('last word')
#print(lst)

#prints the l in apple
#print(x[1][3])

#prints apple:true
#print(x[1:5])

#for element in lst:
#    print(element)

#for index in range(len(lst)):
#    print(lst[index])


#you can type cast with list ahhhhhhhh

y = list('awihduiawhduiwahdu')

#print(y)

#write a function that takes a sentence as a paramater and returns all of the words in that sentence

def word_counter(sentence):
    return sentence.split()

def sentence_to_words(sentence):
    word_lst = []
    #find the words
    found_word = ''

    #add them to list
    word_lst.append(found_word)

    return word_lst


def sentence_to_words(sentence):
    word_lst = []
    found_word = ''
    for letter in sentence:
        if letter == ' ':
            word_lst.append(found_word)
            found_word = ''
        else:
            found_word += letter
    word_lst.append(found_word)

    return word_lst


words = sentence_to_words('cats and dogs are fun')
for word in words:
    print(word)