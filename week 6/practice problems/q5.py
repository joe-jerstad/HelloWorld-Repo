def halistone_seq(n):
    hali_lst = [n]

    while n != 1:
        if n % 2 == 0:
            n /= 2
            hali_lst.append(int(n))
        else:
            n = (n * 3) + 1
            hali_lst.append(int(n))

    return hali_lst

print(halistone_seq(25))

print(halistone_seq(40))