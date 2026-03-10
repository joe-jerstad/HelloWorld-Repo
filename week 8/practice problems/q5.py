def find_relation(name=''):
    relations = {
        'Darth Vader' : 'Father',
        'Leia' : 'Sister',
        'Han' : 'Brother in law',
        'R2D2' : 'Droid'
    }

    if name not in relations:
        return 'Unknown'
    else:
        return relations[name]
    
print(find_relation('Darth Vader'))
print(find_relation('R2D2'))
print(find_relation('Jabba the Hutt'))
print(find_relation())