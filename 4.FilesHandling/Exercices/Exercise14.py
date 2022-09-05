# -------------------------------------------------------------------------------------------------------------
# Exercise #14: Files Handling 
# Developer:    Amr Gaafer
# Date          05.09.2022
# -------------------------------------------------------------------------------------------------------------

import os   # import operating system module

print("Task#1: Files Creation and Directory Inquiries:")
for i in range(1,51):
    if i != 25:
        open('txt'+str(i)+'.txt', 'x')
        myFile = open('txt'+str(i)+'.txt', 'w')
        myFile.write(f'Elzero Web School => {i}')
        myFile.close()
    else:
        open('special-text'+'.txt', 'x')
# get the current working directory
print("Current working directory:\n" + os.getcwd())
# get the absolute directory of the currently opened Python file
print("\nOpened python file directory:\n" + os.path.dirname(os.path.abspath(__file__) ))
# get the name of the currently opened Python file
print("\nOpened python file directory:\n" + os.path.basename(__file__))
# get the number of files within the current directory
print(len([name for name in os.listdir('.') if os.path.isfile(name)]))

print("Task#2: File Append:")
myFile = open('txt1.txt', 'a')
for i in range(0,50):
    myFile.write('\nAppended => Elzero Web School')
myFile.close()

print("Task#3: File Statistical information:")
myFile = open('txt1.txt', 'r+')
linesNr = len(myFile.readlines())       # [Saving] Counting the number of the read lines
myFile.seek(0)                          # Reseting the cursor to the file beginning
read_data = myFile.read()               # Reading the whole file
per_word = read_data.split()            # Splittng the read file into words
wordsNr = len(per_word)                 # [Saving] Counting the number of the read words
charsNr = len(read_data)                # [Saving] Counting the number of the read characters
lCounts = 0
for myChar in read_data:
    if myChar == 'l': lCounts += 1      # [Saving] Counting the number of the read character 'l'

myFile.write(f'\nNumber Of Lines is => {linesNr}')
myFile.write(f'\nNumber Of Words is => {wordsNr}')
myFile.write(f'\nNumber Of Chars is => {charsNr}')
myFile.write(f'\nNumber Of "l" Char  is => {lCounts}')
myFile.close()

print("Task#3: Files Removing:")
for i in range(41,51):
    os.remove('txt'+str(i)+'.txt')
