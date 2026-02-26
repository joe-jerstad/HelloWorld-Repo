def total_donations(donations):
    total = 0

    for person in donations:
        total += donations[person]

    return total

print(total_donations({'John' : 100, 'Sarah' : 200, 'Mike' : 50}))

