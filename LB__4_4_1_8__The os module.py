""" Scenario
    It goes without saying that operating systems allow you to search for files and directories.
While studying this part of the course, you learned about the functions of the os module,
which have everything you need to write a program that will search for directories in a given location.
    To make your task easier, we have prepared a test directory structure for you:
    -- tree > c > other_courses > cpp
    -- tree > c > other_courses > python

    -- tree > cpp > other_courses > c
    -- tree > cpp > other_courses > python

    -- tree > python > other_courses > c
    -- tree > python > other_courses > cpp

Your program should meet the following requirements:
    1. Write a function or method called find that takes two arguments called path and dir.
        The path argument should accept a relative or absolute path to a directory where the search should start,
        while the dir argument should be the name of a directory that you want to find in the given path.
        Your program should display the absolute paths if it finds a directory with the given name.
    2. The directory search should be done recursively. This means that the search should also include all
        subdirectories in the given path.

Example input:
    path="./tree", dir="python"
Example output:
    .../tree/python
    .../tree/cpp/other_courses/python
    .../tree/c/other_courses/python
"""
import os


class MakeTree:
    def __init__(self):
        self.parent_dir = "C:\\Users\\olly1215\\Desktop\\Geek"
        self.new_path = ''

    def make_dir(self, directory):
        self.new_path = self.parent_dir
        for i in directory:
            self.new_path = os.path.join(self.new_path, i)
            if os.path.exists(self.new_path):
                continue
            else:
                os.mkdir(self.new_path)
        print("New Directory path <'% s'> was created " % self.new_path)


class SearchFolder:
    pass


class RemoveTree:
    pass


tree = 'tree'
c = 'c'
cpp = 'cpp'
python = 'python'
other_courses = 'other_courses'

newPath = MakeTree()

path_1_1 = [tree, c, other_courses, cpp]
path_1_2 = [tree, c, other_courses, python]
path_2_1 = [tree, cpp, other_courses, c]
path_2_2 = [tree, cpp, other_courses, python]
path_3_1 = [tree, python, other_courses, c]
path_3_2 = [tree, python, other_courses, cpp]

dir_list = [path_1_1, path_1_2, path_2_1, path_2_2, path_3_1, path_3_2]
for lis_dir in dir_list:
    newPath.make_dir(lis_dir)

# path = input("Enter path, like: <./path> :")
# directory = input("Enter directory, like: <dir> :")
