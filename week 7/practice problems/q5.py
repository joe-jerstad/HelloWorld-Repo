def count_repetitions(elements):
    seen = {}

    for ele in elements:
        if ele not in seen:
            seen[ele] = 1
        else:
            seen[ele] += 1

    return seen

test_1 = ['cat', 'dog', 'cat', 'cow', 'cow', 'cow']
test_2 = [1,5,5,5,12,12,0,0,0,0,0,0]

print(count_repetitions(test_2))

