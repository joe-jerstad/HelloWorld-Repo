
'''
def first_letters(sentence):
    new_string = ''
    words_list = sentence.split()
    for word in words_list:
        new_string += word[0]
    return new_string

    
print(first_letters('wingardium leviosa makes objects float'))
'''

#try solution by using a flag that starts a true to collect first letter, goes false, turns true when there is a space to continue to collect letters

#IMPORTANT HOW ENUMERATE WORKS
'''

lyst = ['word1', 'word2', 'word3', 'word4', ]

for element in lyst:
    print(element)

for index in range(len(lyst)):
    print(lyst[index])

for index, element in enumerate(lyst):
    print(index, element)
'''

#really cool solution

def first_letters(sentence):
    new_word =''
    flag = True
    for letter in sentence:
        if flag:
            new_word += letter
            flag = False
        if letter == ' ':
            flag = True
    return new_word

print(first_letters('wingardium leviosa makes objects float'))