# --------------------------------------------------------------------------------------------------
# Files Handling:
#   File Opening:
#       open("file name with its directory", "mode")
#           returns a <class '_io.TextIOWrapper'> object (e.g. myFile)
#       the different modes of this command:
#           "r" Read        [Default value] open a file to read and give an error if the file does not exist
#           "w" Write       open a file to write, create a file if it does not exist
#           "a" Append      open a file to append values, create a file if does not exist
#           "x" Create      create a file and give an error if the file exists
#
#   Reading Methods:
#       myFile.read(n)      Read the whole file or till the maximum number of characters (n) is reached
#       myFile.readline(n)  Read the whole line or till the maximum number of characters (n) is reached
#       myFile.readlines(n) Read the whole file as a list as long as the n character reaches this list item
#
#   Writing/Appending Methods:
#       myFile.write(s)     Write the given string (s) in the file
#       myFile.writelines(s)Write the given string list (s) in the file
#   Writing vs. Append:
#       Write rewrites the whole file with every execution. Append starts from the end of the text file.
#
#   File Closing:
#       myFile.close()
#
#   File Opening and Closing using special syntax:
#       with open("file name with its directory", "mode") as f:
#           block of code (e.g. f.read())
#       -This with keyword allows to open a file, do operations on it,
#        and automatically close it after the indented code is executed.
#        f.close() is not needed anymore!
#        the file object f can only be accessed within this indented block.
#
#   Important Methods on opened files:
#       myFile.truncate(n)  Remove the whole text except the first n given characters [only in Append Mode]
#       myFile.tell()       Return the position of the cursor
#       myFile.seek(n)      Move the curser with the given offset value
#       - Opening a file is like openning a window to look into the file.
#         To be more precise, it'S a window that'S only one character wide 
#         and it always starts off at the very start of the file.
#         -> the same file can be opened many times
# --------------------------------------------------------------------------------------------------

import os   # import operating system module
os.system('cls')        # cls command

# get the current working directory
print("\nCurrent working directory:\n" + os.getcwd())

# get the absolute path of the currently opened Python file
print("\nOpened python file path:\n" + os.path.abspath(__file__))
print(__file__)

# get the absolute directory of the currently opened Python file
print("\nOpened python file directory:\n" + os.path.dirname(os.path.abspath(__file__) ))

# change the current working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print('\n# ********************************************* #')
print('File Opening:\n')
# absolute path
# myFile = open("D:/..../MyCode/4.FilesHandling/myFileRead.txt.txt")
# relative path -> it can be used after change of the current working directory
myFile = open("myFileRead.txt")

# tests and checks:
print(myFile)           # Data object (name, mode and encoding)
print(type(myFile))     # Object type <class '_io.TextIOWrapper'>
print(myFile.name)
print(myFile.mode)
print(myFile.encoding)

# crash test to open the same file many times
# <module> OSError: [Errno 24] Too many open files: 'myFileRead.txt'
# files = []
# for i in range(10000):
#     files.append(open('myFileRead.txt', 'r'))
#     print(i)

print('\n# ********************************************* #')
print('File Reading:\n')
print(myFile.read())
# print(myFile.read(7))
# print(myFile.readline(8))
# print(myFile.readlines())
myFile.close()

with open("myFileRead.txt") as f:
    print('\n\'with\' syntax:')
    for line in f:
        print(line, end='')
    print('')

print('\n# ********************************************* #')
print('File Writing/Appending:\n')
myFile = open("myFileWrite.txt", "w")
myFile.write("Hi Amr!\n")
myFile.write("You are doing this right\n")
myFile.close()

myFile = open("myFileWrite.txt", "a")
myFile.writelines(["Hi Amr once more!\n", "You are doing this really right\n"])
myFile.close()

print('\n# ********************************************* #')
print('File Creation:\n')
myFile = open("myFileCreated.txt", "x")
myFile = open("myFileCreated.txt", "w")
myFile.write("No Way!")
myFile.close()
os.remove("myFileCreated.txt")

print('\n# ********************************************* #')
print('Important Notes:\n')
print('truncate:')
myFile = open("myFileRead2.txt", 'a')
myFile.truncate(7)              # Remove the whole text except the first n given characters
myFile.close()

print('tell:')
myFile = open("myFileRead.txt", 'r')
print(myFile.tell())            # Return the position of the cursor (valid for all open modes)
print(myFile.readline())
print(myFile.tell())
myFile.close()

print('seek:')
myFile = open("myFileRead.txt")
myFile.seek(9)                  # Move the curser with the given offset value
print(myFile.read())
myFile.close()
