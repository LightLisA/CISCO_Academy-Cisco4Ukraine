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
    src = open(srcname, 'rt', encoding='utf-8')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)


dictionary_with_num = {}

try:
    readin = src.read()
    for key in readin:
        cnt = 0
        lowKey = key.lower()
        if lowKey in dictionary_with_num:
            continue
        else:
            if lowKey.isalpha():
                for chart in readin:
                    lowChart = chart.lower()
                    if lowKey == lowChart:
                        cnt += 1
                dictionary_with_num[lowKey] = cnt
            else:
                continue
    src.close()
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)

dictList = sorted(dictionary_with_num.keys())
for i in dictList:
    print(str(i) + " --> " + str(dictionary_with_num[i]))

src.close()
