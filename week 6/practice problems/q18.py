def lag_days(miles):
    lag = 0

    for i in range(len(miles) - 1):
        if miles[i] > miles[i + 1]:
            lag += 1
            
    return lag

print(lag_days([5,3,2,1]))
print(lag_days([10,11,12,9,10]))
print(lag_days([6,5,4,3,2,9]))
print(lag_days([9,9]))
