def highway_directions(hgwy_num):
    if hgwy_num >= 1000 or hgwy_num % 100 == 0 or hgwy_num <= 0:
        return f'I-{hgwy_num} is an invalid highway number'
    elif hgwy_num % 2 == 0:
        return f'I-{hgwy_num} runs east/west'
    elif hgwy_num % 2 == 1:
        return f'I-{hgwy_num} runs north/south'

print(highway_directions(42))

