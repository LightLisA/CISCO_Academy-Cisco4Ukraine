# importing os module
import os
import platform

print(os.name)
print(platform.uname(), '\n')
# uname function -  returns an object containing information about the operating system
# Unfortunately, the uname function only works on some Unix systems. If you use Windows,
# you can use the uname function in the "platform" module, which returns a similar result.
#
""""
    systemname — stores the name of the operating system;
    nodename — stores the machine name on the network;
    release — stores the operating system release;
    version — stores the operating system version;
    machine — stores the hardware identifier, e.g., x86_64.
    
    posix — you'll get this name if you use Unix;
    nt — you'll get this name if you use Windows;
    java — you'll get this name if your code is written in Jython.

"""
# ###################################################################################
# Python program to explain os.mkdir() method
# Directory
directory = "GeeksforGeeks"
# Parent Directory path parent_dir = "D:/Pycharm projects/"
parent_dir = "C:\\Users\\olly1215\\Desktop\\Geek"
# Path
path = os.path.join(parent_dir, directory)
# Create the directory 'GeeksForGeeks' in '/home / User / Documents'
os.mkdir(path)
print("Directory '% s' created" % directory)
'''# Directory
directory = "Geekss"
# Parent Directory path
parent_dir = "C:\\Users\\olly1215\\Desktop\\Geek"
# mode
mode = 0o666
# Path
path = os.path.join(parent_dir, directory)
# Create the directory 'GeeksForGeeks' in '/home / User / Documents' with mode 0o666
os.mkdir(path, mode)
print("Directory '% s' created" % directory)'''

# ###################################################################################
my_first_directory = "C:\\Users\\olly1215\\Desktop\\Geek\\my_first_directory"
os.mkdir(my_first_directory)  # створити одну діректорію
print("GET CWD ::  ", os.getcwd())  # отримати шлях де ти є зараз
print("LIST DIR ::  ", os.listdir(), '\n')  # отримати список об'єктів із діректорії де ти є зараз
"""
    my_first_directory — this is a relative path which will create the my_first_directory directory in the current working directory;
    ./my_first_directory — this is a relative path that explicitly points to the current working directory. It has the same effect as the path above;
    ../my_first_directory — this is a relative path that will create the my_first_directory directory in the parent directory of the current working directory;
    /python/my_first_directory — this is the absolute path that will create the my_first_directory directory, which in turn is in the python directory in the root directory.
"""
# ###################################################################################
my_second1_directory = "C:\\Users\\olly1215\\Desktop\\Geek\\my_first_directory\\my_second1_directory"
os.makedirs(my_second1_directory)  # створити декілька папок
print("GET CWD 0000 ::  ", os.getcwd())

os.chdir(parent_dir)
print("GET CWD 1111 ::  ", os.getcwd())

os.chdir("my_first_directory")
print("GET CWD 2222 ::  ", os.getcwd())
print("LIST DIR 2nd1  ::  ", os.listdir(), '\n')
# ###################################################################################
my_second2_directory = "C:\\Users\\olly1215\\Desktop\\Geek\\my_first1_directory\\my_second2_directory"
os.makedirs(my_second2_directory)
os.chdir("C:\\Users\\olly1215\\Desktop\\Geek\\my_first1_directory")
print("GET CWD 1st ::  ", os.getcwd(), '\n')

os.chdir("my_second2_directory")
print("GET CWD 2nd ::  ", os.getcwd(), '\n')

# #################################################################################################################
""" REMOVAL DIR """
os.mkdir("C:\\Users\\olly1215\\Desktop\\Geek\\my_first3_directory")
os.makedirs("C:\\Users\\olly1215\\Desktop\\Geek\\my_first4_directory\\my_second_directory")
os.chdir("C:\\Users\\olly1215\\Desktop\\Geek")
print(os.listdir())

os.rmdir("C:\\Users\\olly1215\\Desktop\\Geek\\my_first3_directory")  # rmdir -  удалить одну папку
print(os.listdir())
print("Directory '% s' -- deleted" % "my_first3_directory", '\n')

os.removedirs("my_first4_directory\\my_second_directory")  # removedirs - декілька папок
print(os.listdir())
print("Directory '% s' -- deleted" % "my_first4_directory", '\n')

os.removedirs("my_first_directory\\my_second1_directory")
print(os.listdir())
print("Directory '% s' -- deleted" % "my_first_directory", '\n')

os.removedirs("my_first1_directory\\my_second2_directory")
print(os.listdir())
print("Directory '% s' -- deleted" % 'my_first1_directory', '\n')

print(os.listdir())
os.rmdir(directory)
print("Directory '% s' -- deleted" % directory, '\n')


print(os.getcwd())
print(os.listdir())

# #########################################################################################
''' SYSTEM function '''
# All functions presented in this part of the course can be replaced by a function called "system", which executes a
#   command passed to it as a string. The system function is available in both Windows and Unix.
# Depending on the "system", it returns a different result.
# In Windows, it returns the value returned by the shell after running the command given, while in Unix,
#   it returns the exit status of the process.
# The above example will work in both Windows and Unix. In our case, we receive exit status 0, which indicates success
returned_value = os.system("mkdir C:\\Users\\olly1215\\Desktop\\Geek\\my_first5_directory")
print("returned_value ---------     ", returned_value, '\n')
remove_value = os.system("rmdir my_first5_directory")
print("returned_value ---------     ", remove_value)
print("Directory '% s' -- deleted" % 'my_first5_directory', '\n')


