from os import strerror

try:
    fo = open('C:\\Users\\olly1215\\Desktop\\newtext.txt', 'wt') # A new file (newtext.txt) is created.
    for i in range(10):
        s = "line #" + str(i+1) + "\n"
        for ch in s:
            fo.write(ch)
    fo.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))


try:
    fo = open('C:\\Users\\olly1215\\Desktop\\newtext.txt', 'wt')
    for i in range(10):
        fo.write("line #" + str(i+11) + "\n")
    fo.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))


import sys
sys.stderr.write("Error message")
