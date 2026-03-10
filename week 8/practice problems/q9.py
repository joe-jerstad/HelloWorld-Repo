def get_indices(nums, value=0):
    indices = []

    for i, num in enumerate(nums):
        if num == value:
            indices.append(i)

    return indices

print(get_indices([1,0,5,0,7]))
print(get_indices([1,5,5,2,7], 7))
print(get_indices([1,5,5,2,7]))
print(get_indices([1,5,5,2,7], 5))
print(get_indices([1,5,5,2,7], 8))
print(get_indices(['a', 'a', 'b', 'a', 'b', 'a'], 'a'))

