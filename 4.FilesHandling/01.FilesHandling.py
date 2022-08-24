# -------------------------------------------------------------------------------------------------------------
# Files Handling:
#   open("file name with its directory", "mode")
#       returns a <class '_io.TextIOWrapper'> object (e.g. myFile)
#       the different modes of this command:
#           "a" Append      open a file to append values, create a file if does not exist
#           "r" Read        [Default value] open a file to read and give an error if the file does not exist
#           "w" Write       open a file to write, create a file if it does not exist
#           "x" Create      create a file and give an error if the file exists
#
#   Reading Methods:
#       myFile.read(n)          Read the whole file or till the maximum number of characters (n) is reached
#       myFile.readline(n))     Read the whole line or till the maximum number of characters (n) is reached
#       myFile.readlines())     Read the whole file as a listas long as the n character reaches this list item
#
#   Writing Methods:
#       myFile.write(String)            Write the given string in the file
#       myFile.writelines(StringList)   Write the given string list in the file
#   Writing vs. Append:
#       Write rewrites the whole file with every execution. Append starts from the end of the text file.
#
#   Important Methods:
#   myFile.truncate(n):
#       Remove the whole text except the first n given characters [only in Append Mode]
#   myFile.tell():
#       Return the position of the cursor [valid for all open modes]
#   myFile.seek():
#       Move the curser with the given offset value [valid for all open modes]
#
#   myFile.close("file name with its directory")
# -------------------------------------------------------------------------------------------------------------

import os   # import operating system module

# get the current working directory
print("\nCurrent working directory:\n" + os.getcwd() + "\n")

# get the absolute path of the currently opened Python file
print("\nOpened python file path:\n" + os.path.abspath(__file__) + "\n")

# get the absolute directory of the currently opened Python file
print("\nOpened python file directory:\n" + os.path.dirname(os.path.abspath(__file__) ) + "\n")

# change the current working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print('\n# ********************************************* #')
print('File Opening:\n')
# absolute path
# myFile = open("D:/Career Development/Nanodegree_Python/__Elzero Web School__/MyCode/4.FilesHandling/amr.txt")
# relative path
myFile = open("myFileRead.txt")

# tests and checks:
print(myFile)           # Data object (name, mode and encoding)
print(type(myFile))     # Object type <class '_io.TextIOWrapper'>
print(myFile.name)
print(myFile.mode)
print(myFile.encoding)

print('\n# ********************************************* #')
print('File Reading:\n')
# print(myFile.read(7))         # Read the whole file or till the maximum number of characters is reached
print(myFile.read())

# print(myFile.readline())      # Read the whole line or till the maximum number of characters is reached
# print(myFile.readlines(15))     # Read the whole file as a list or till the maximum number of characters is reached
myFile.close()

print('\n# ********************************************* #')
print('File Writing/Appending:\n')
myFile = open("myFileWrite.txt", "w")
myFile.write("Hi Amr!\n")
myFile.write("You are doing this right\n")
myFile.close()

myFile = open("myFileWrite.txt", "a")
myFile.write("Hi Amr once more!\n")
myFile.write("You are doing this really right\n")
myFile.close()

print('\n# ********************************************* #')
print('Important Notes:\n')
print('truncate:\n')
myFile = open("myFileRead2.txt", 'a')
myFile.truncate(7)              # Remove the whole text except the first n given characters
myFile.close()

print('tell:\n')
myFile = open("myFileRead.txt", 'r')
print(myFile.tell())            # Return the position of the cursor (valid for all open modes)
print(myFile.readline())
print(myFile.tell())
myFile.close()

print('seek:\n')
myFile = open("myFileRead.txt")
myFile.seek(7)                  # Move the curser with the given offset value
print(myFile.read())
myFile.close()

print('\n# ********************************************* #')
print('File Creation:\n')
myFile = open("myFileReadCreated.txt", "x")
myFile = open("myFileReadCreated.txt", "w")
myFile.write("No Way!")
myFile.close()
os.remove("myFileReadCreated.txt")
