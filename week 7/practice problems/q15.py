def majority_element(nums):
    num_count = {}

    for num in nums:
        if num not in num_count:
            num_count[num] = 1
        else:
            num_count[num] += 1

    for i in num_count:
        if num_count[i] > len(num_count) // 2:
            return i
        
print(majority_element([2,2,1,1,1,2,2]))
print(majority_element([2,2,3,2,1,2,1,4,4,1,2,2]))