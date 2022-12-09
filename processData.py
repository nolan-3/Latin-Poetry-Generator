import csv
table = [{'a': 7, 'b':5, 'c': 6}] #... 
# csv file name
filename = "rawData.csv"
#alphabet = ['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z']
letter = ''
tables = list()
i = 0
j = 0
running = True
numTablesToAdd = 4

def findFirstLetter(string):
    letter = ''
    for i in range(0, len(string)):
        if string[i] != '':
            return string[i].lower()


def deleteFirstLetter(letter):
    string = ''
    searchingForFirstLetter = True
    for i in range(0, len(string)):
        if string[i] == letter:
            None
        else:
            string += string[i]


    
dictionary = dict()
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting each data row one by one
    for row in csvreader:
        if (j % 24 == 0 and j != 0):
            tables[i] = dictionary
            #get the first letter from text file (the key/letter a-z)
            #and the rest of the csv value (the value/half line of poetry)
            key = findFirstLetter(row)
            value = deleteFirstLetter(key)
            dictionary[letter] = value
            if(letter):
                tables[i] = dictionary
                i += 1
                break

    


 
#TO output [dictionary1, dictionary2, dictionary3]