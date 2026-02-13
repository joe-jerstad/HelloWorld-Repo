
'''
number = 5
while number <= 100:
    if number % 2 == 0:
        print(number)
    number += 1

for number in range(5, 101):
    if number % 2 == 0:
        print(number)


word = 'aple'

for letter in word:
    print(letter)


#count the number of r's in strawberry
 

word = 'strawberry'
total = 0

for letter in word:
    if letter == 'r':
        total += 1

print(f"The number of r's in {word} is {total}.")

word = 'tastie taco time'
total = 0

for letter in word:
    if letter == 't':
        total += 1

print(f"The number of r's in {word} is {total}.")


#my version of func:


def letter_count(word, letter):
    count = 0
    for i in word:
        if i == letter:
            count += 1
    return f"The amount of {letter}'s in {word} is {count}."

print(letter_count('well watermelon takes swell', 'l'))


#def function_name(parameters):
    #what you want your function to do

#teacher func


word = 'well watermelon takes swell'

def count_letters(word, test_letter):
    total = 0

    for letter in word:
        if letter == test_letter:
            total += 1

    print(f"The number of {test_letter}'s in {word} is {total}.")

word = "well watermelon takes swell"
count_letters(word, 'l')

word = "tastie taco time"
count_letters(word, 't')

word = "strawberry"
count_letters(word, 'r')


#write a function that prints the even numbers between a lower_bound and an upper_bound, call that function even_printer, call it with the values 2, 10
#3 and 15, 7 and 20


def even_printer(lower_bound, upper_bound):
    for number in range(lower_bound, upper_bound + 1):
        if number % 2 == 0:
            print(number, end = ' ') 
    print()

even_printer(2,10)
even_printer(3,15)
even_printer(7,20)





break = take the false path of the condition and end the loop early
continue = 



#determine if the folliwng word has the letter 'a'


word1 = 'tablespoonful'
word2 = 'technology'

a_appears = False
    
for letter in word1:
    if letter == 'a':
        a_appears = True
        break

if a_appears:
    print(f'Yes, the word {word1} has an a.')
else:
    print(f'No, the word {word1} does not have an a.')


#indexing

word1 = 'apple'

#write code to print the l

print(word1[3])

#write code to print the y and the t

word2 = 'happy times'
print(word2[4])
print(word2[5])
print(word2[6])
print(word2[7])

print('\n======================\n')

for index in range(4,8):
    print(word2[index], end = '')

print('\n======================\n')

print(word2[4:8])

print(word2[6:])


#len - reports the length of ana object(the word).

word2 = 'happy times'

print(len(word2))

word = 'hello world'

for index in range(0,len(word)):
    print(index, word[index])
'''

#write code to determine how many vowels are in a word
#aeiouy

def count_vowels(word):
    count = 0

    for letter in word:
        if letter in 'aeiouy':
            count += 1
    return count

def new_count_vowels(word):
    count = 0
    for letter in word:
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'y':
            count += 1
    return count

print(new_count_vowels('word with vowels'))

