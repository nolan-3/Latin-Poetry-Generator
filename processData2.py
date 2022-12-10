#each new line is an entry to the dicionary

import csv
table = [{'a': 7, 'b':5, 'c': 6}] #... 
# csv file name
filename = "rawData.csv"
tables = list()
dictionary = dict()

#returns the first non-space character in a string
def findFirstLetter(string):
    letter = ''
    for i in range(0, len(string)):
        if string[i].isalpha():
            return string[i].lower()

def deleteFirstLetter(string):
    newString = ''
    searchingForFirstLetter = True
    for i in range(0, len(string)):
        if searchingForFirstLetter == True and string[i].isalpha():
            searchingForFirstLetter = False
            #only append characters after the first character
        elif searchingForFirstLetter == False:
            newString += string[i]
    return newString

# Using readlines()
with open('rawData.txt', 'r') as file1, open('newFile.txt', 'a') as file2:
    Lines = file1.readlines()
    #start new file
    file2.write('[{')

    for line in Lines:
        #if the previous code table is over create a new one
        if(len(line) == 1):
            file2.write('},\n{')
            continue
        else:
            print(len(line))
            file2.write(findFirstLetter(line) + ':' + deleteFirstLetter(line))
        #end new file
    file2.write('}]')