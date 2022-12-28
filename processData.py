# takes in code book lines separated by whitespace 
# and return this desired output:
table = [{'a': 7, 'b':5, 'c': 6}] #... 

#returns the first non-space character in a string
def findFirstLetter(string):
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
    return newString.strip()

# Using readlines()
with open('rawData.txt', 'r') as file1, open('newFile.py', 'a') as file2:
    Lines = file1.readlines()
    #start new file
    file2.write('[{')

    for line in Lines:
        #if the previous code table is over create a new one
        if(len(line) == 1):
            file2.write('},\n{')
            continue
        else:
            string = '\'{}\':\'{}\',\n'.format(findFirstLetter(line), deleteFirstLetter(line))
            #string = '\'' + findFirstLetter(line) + '\'' + ':\'' + deleteFirstLetter(line) + ','
            print(string)
            file2.write(string)
        #end new file
    file2.write('}]')
