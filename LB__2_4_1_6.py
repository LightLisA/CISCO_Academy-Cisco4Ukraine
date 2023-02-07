dictionary_with_num = {
    '1': ['  #', '  #', '  #', '  #', '  #'],
    '2': ['###', '  #', '###', '#  ', '###'],
    '3': ['###', '  #', '###', '  #', '###'],
    '4': ['# #', '# #', '###', '  #', '  #'],
    '5': ['###', '#  ', '###', '  #', '###'],
    '6': ['###', '#  ', '###', '# #', '###'],
    '7': ['###', '  #', '  #', '  #', '  #'],
    '8': ['###', '# #', '###', '# #', '###'],
    '9': ['###', '# #', '###', '  #', '###'],
    '0': ['###', '# #', '# #', '# #', '###']
}


def parsing_numbers(entered_num):
    if entered_num.isdigit():
        for num in range(5):
            new_list = []
            for i in (str(entered_num)):
                new_list.append(dictionary_with_num[i][num])

            print(' '.join(new_list))
    else:
        print("You introduced symbols differ from numbers")


parsing_numbers(input("Enter number from 0 to 9: "))

