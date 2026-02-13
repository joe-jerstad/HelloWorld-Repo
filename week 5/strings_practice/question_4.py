def hamming_distance(word1, word2):
    index = 0
    distance = 0
    for letter in word1:
        if letter != word2[index]:
            distance += 1
        index += 1
    return distance

print(hamming_distance('strong', 'strung'))