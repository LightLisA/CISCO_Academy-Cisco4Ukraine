"""
Scenario
    Prof. Jekyll conducts classes with students and regularly makes notes in a text file. Each line of the
  file contains three elements: the student's first name, the student's last name, and the number of point the student
  received during certain classes. The elements are separated with white spaces. Each student may appear more than once
  inside Prof. Jekyll's file.

The file (samplefile.txt) may look as follows:
    John	Smith	5
    Anna	Boleyn	4.5
    John	Smith	2
    Anna	Boleyn	11
    Andrew	Cox	1.5

Your task is to write a program which:
-- asks the user for Prof. Jekyll's file name;
-- reads the file contents and counts the sum of the received points for each student;
-- prints a simple (but sorted) report, just like this one:

output:
    Andrew Cox 	 1.5
    Anna Boleyn 	 15.5
    John Smith 	 7.0

Note:
    your program must be fully protected against all possible failures: the file's non-existence, the file's
    emptiness, or any input data failures; encountering any data error should cause immediate program termination,
    and the erroneous should be presented to the user; implement and use your own exceptions hierarchy - we've presented
    it in the editor; the second exception should be raised when a bad line is detect, and the third when the source file
    exists but is empty.

Tip: Use a dictionary to store the students' data.
"""
from os import strerror
import sys


class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    def bad_value(self, value):
        if not value.isalpha() and not value.isdigit() and value != '\t' and value != '.' and value != ' ' \
                and value != '\n':
            print("File has incorrect characteristics! ->: {}".format(value))
            sys.exit()


class FileEmpty(StudentsDataException):
    def empty_file(self, filename):
        try:
            myfile = open(filename)
        except IOError:  # FileNotFoundError in Python 3
            print("File not found: {}".format(filename))
            sys.exit()

        contents = myfile.read()
        myfile.close()

        if not contents:
            print("{} : File is EMPTY!".format(filename))
            sys.exit()


emptyclass = FileEmpty()
badchart = BadLine()

student_dictionary = {}
try:
    file_name = 'C:\\Users\\olly1215\\Desktop\\empty_file.txt'
    openfile = open(file_name, 'rt')
    lines = openfile.readlines(20)

    emptyclass.empty_file(file_name)

    while len(lines) != 0:
        for line in lines:
            key = ''
            value = ''
            for ch in line:
                badchart.bad_value(ch)
                if ch.isalpha() or ch == '\t':
                    if ch == '\t':
                        key += ' '
                    else:
                        key += ch
                elif ch.isdigit() or ch == '.':
                    value += ch

            if key in student_dictionary:
                student_dictionary[key] = float(student_dictionary[key]) + float(value)
            else:
                student_dictionary[key] = value
        lines = openfile.readlines(10)
    openfile.close()
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)

sorted_dictionary = sorted(student_dictionary.keys())  # зробив у алфавітному порядку словник
for i in sorted_dictionary:  # вивожу словник на екран
    print(i + " " + str(student_dictionary[i]))
