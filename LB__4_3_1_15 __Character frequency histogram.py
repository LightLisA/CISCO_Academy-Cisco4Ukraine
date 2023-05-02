# Scenario
#    A text file contains some text (nothing unusual) but we need to know how often (or how rare)
#    each letter appears in the text. Such an analysis may be useful in cryptography, so we want
#    to be able to do that in reference to the Latin alphabet.
#
# Your task is to write a program which:
#    asks the user for the input file's name;
#    reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
#    prints a simple histogram in alphabetical order (only non-zero counts should be presented)
#
# Create a test file for the code, and check if your histogram contains valid results.
# Tip: We think that a dictionary is a perfect data collection medium for storing the counts.
#       The letters may be keys while the counters can be values.
#

# C:\Users\Aleksey\Desktop\text.txt
# C:\Users\olly1215\Desktop\text.txt

from os import strerror

# srcname = input("Enter the source file name: ")
srcname = 'C:\\Users\\olly1215\\Desktop\\text.txt'
try:
    src = open(srcname, 'rt', encoding='utf-8')         # відкриваю файл; rt - читаю текст;
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)


dictionary_with_num = {}                                # створюю пустий словник

try:
    readin = src.read()                                 # читаю файл
    for key in readin:
        cnt = 0                                         # створюю сщотчик
        lowKey = key.lower()                            # перевожу все в нижній регістр
        if lowKey in dictionary_with_num:
            continue                                    # якщо запис уже є в словнику. то скіпаю його
        else:
            if lowKey.isalpha():                        # якщо символ є буквою, то ...
                for chart in readin:
                    lowChart = chart.lower()
                    if lowKey == lowChart:              # порівнюю перше значення із файлу, з усіма символами у файлі
                        cnt += 1
                dictionary_with_num[lowKey] = cnt       # записую в словник
            else:
                continue
    src.close()
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)

dictList = sorted(dictionary_with_num.keys())           # зробив у алфавітному порядку словник
for i in dictList:                                      # вивожу словник на екран
    print(str(i) + " --> " + str(dictionary_with_num[i]))

src.close()                                             # закриваю сесію - ОБОВ'ЯЗКОВО
