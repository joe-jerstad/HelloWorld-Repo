def first_letters(sentence):
    firsts = ''

    firsts += sentence[0]

    for i in range(len(sentence) - 1):
        if sentence[i] == ' ':
            firsts += sentence[i + 1]
    
    return firsts


print(first_letters('wing lev mak obj float'))
        

