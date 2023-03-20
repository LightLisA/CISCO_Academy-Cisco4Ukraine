first_row = 'modern'

second_row = 'norman'

comp = ''

if len((first_row.lower()).replace(' ', '')) == len((second_row.lower()).replace(' ', '')):
    for char in first_row:
        for chart in second_row:
            if char.lower() == chart.lower():
                comp += ''.join(chart)

    if (first_row.lower()).replace(' ', '') == (comp.lower()).replace(' ', ''):
        print("Anagrams")
    else:
        print("Not anagrams 2")
else:
    print("Not anagrams 1")