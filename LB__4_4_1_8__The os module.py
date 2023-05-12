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


def make_dir(directory):  # створюємо ієрархію із папок яку задали нижще
    new_path = parent_dir
    for i in directory:
        new_path = os.path.join(new_path, i)
        if os.path.exists(new_path):
            # print("The Directory <'% s'> exists " % i)
            continue
        else:
            os.mkdir(new_path)
    print("** New Directory path <'% s'>   created " % new_path)


def dir_list_folder(head_dir, dir_name):    # шукаємо потрібну папку через рукурсію
    dirList = []
    for fn in os.listdir(head_dir):     # список папок у Папці
        dirfile = os.path.join(head_dir, fn)    # з'єднуємо парент шлях і папку
        if os.path.isdir(dirfile):
            if fn.upper() == dir_name.upper():  # порівнюємо поточний каталог із заданой папкой
                dirList.append(dirfile)     # добавляємо в список
            else:
                dirList += dir_list_folder(dirfile, dir_name)   # якщо небуло співпадінь ідемо шукаті далі
    return dirList


def list_folder_for_remove(head_dir):   # удаляемо папки через рукурсію
    for fn in os.listdir(head_dir):
        dirfile = os.path.join(head_dir, fn)
        list_folder_for_remove(dirfile)
        if os.path.isdir(dirfile):
            os.rmdir(dirfile)
            print("***  <% s> removed successfully" % dirfile)


def remove_tree(header_dir):
    print('\n')
    os.chdir(header_dir)
    list_folder_for_remove(header_dir)


tree = 'tree'
c = 'c'
cpp = 'cpp'
python = 'python'
other_courses = 'other_courses'
parent_dir = "C:\\Users\\olly1215\\Desktop\\Geek"

#  ієрархія папов
path_1_1 = [tree, c, other_courses, cpp]
path_1_2 = [tree, c, other_courses, python]
path_2_1 = [tree, cpp, other_courses, c]
path_2_2 = [tree, cpp, other_courses, python]
path_3_1 = [tree, python, other_courses, c]
path_3_2 = [tree, python, other_courses, cpp]

# створили список із шєрархії каталогів і посилаємо на створення
dir_list = [path_1_1, path_1_2, path_2_1, path_2_2, path_3_1, path_3_2]
for lis_dir in dir_list:
    make_dir(lis_dir)
print('\n')

# path = input("Enter path, like: <C:\\Users\\Folder_1\\Folder_2> : ")
# directory = input("Enter directory name, like: <python> or <c> or <cpp>: ")
path = "C:\\Users\\olly1215\\Desktop\\Geek\\tree"
directory = "python"

#  передаємо на пошук потрібну нам папку
list_of_directories = dir_list_folder(path, directory)
if len(list_of_directories) == 0:
    print("The <% s> directory is absent" % directory)
else:
    for item in list_of_directories:
        print(item)

# видаляемо всі каталоги які створили
remove_tree(parent_dir)
