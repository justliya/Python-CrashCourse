ordinal = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for position in ordinal:
    if position == 1:
        suffix = 'st'
    elif position == 2:
        suffix = 'nd'
    elif position == 3:
        suffix = 'rd'
    else:
        suffix = 'th'
    print(str(position) + suffix + '\n')