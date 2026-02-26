def hamming_distance(word1, word2):
    i = 0
    distance = 0
    for l in word1:
        if l != word2[i]:
            distance += 1
        i += 1
    return distance

print(hamming_distance('string', 'strung'))

