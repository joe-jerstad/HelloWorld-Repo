def progress_days(miles):
    progress = 0

    for i in range (len(miles) - 1):
        if miles[i] < miles[i + 1]:
            progress += 1
    
    return progress

print(progress_days([3,4,1,2]))
print(progress_days([10,11,12,9,10]))
print(progress_days([6,5,4,3,2,9]))
print(progress_days([9,9]))
