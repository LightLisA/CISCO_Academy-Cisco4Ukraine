first_row = 'Ten animals I slam in a net'

second_row = first_row[::-1]

if (first_row.lower()).replace(' ', '') == (second_row.lower()).replace(' ', ''):
    print("YRA")
else:
    print("NOPE")
