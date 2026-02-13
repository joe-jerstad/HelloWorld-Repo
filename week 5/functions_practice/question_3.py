def knuts_converter(knuts):
    galleons = knuts // 493
    sickles = (knuts % 493) // 29
    remaining_knuts = (knuts % 493) % 29
    final_string = ''
    if galleons > 0:
        final_string += f'{galleons} galleons '
    if sickles > 0:
        final_string += f'{sickles} sickles '
    if remaining_knuts > 0:
        final_string += f'{remaining_knuts} knuts '
    return final_string
    

print(knuts_converter(993))