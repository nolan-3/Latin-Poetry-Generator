from data import table
import random
import string

#replaces letters not included in the lookup table: j, u, y  
def checkLetter(letter):

    if letter == 'j':
            letter = 'i'
    elif letter == 'u':
            letter = 'v'
    elif letter == 'y':
            letter = 'z'
    return letter


def generate(message):
    message = message.lower().strip()
    poem = ''
    endOfLine = False
    #current index in the string (only counting letters)
    charNum = 0
    #number of dictionaries in the lookup table
    numOfDicts = len(table[0])

    #eliminate letters not included in the table
    tempString = ''
    for i in range(0, len(message)):
        tempString += checkLetter(message[i])
    message = tempString


    for i in range(0, len(message)):
        char = message[i]
        #if message length > number of dictionaries, recycle them
        dictNum = charNum % numOfDicts
        #isalpha() isn't necessary but its a nice tool to have
        if char.isalpha() and ord(char) >= 97 and ord(char) <= 122:
            print(dictNum)
            print(char)
            print("table[-][dictNum]")
            print(table[0][dictNum])
            halfLine = table[0][dictNum][char][0]
            #print a new line if at the end of a line of latin
            if(endOfLine):
                #print(halfLine)
                poem += halfLine + '\n'
                endOfLine = False
            else:
                poem += halfLine + ' '
                #print(halfLine + " ", end='')
                endOfLine = True
            charNum += 1
    #make sure the final line is complete
    if(endOfLine):
        dictNum = charNum % numOfDicts
        char = random.choice(string.ascii_letters).lower()
        char = checkLetter(char)
        poem += table[0][dictNum][char][0]
    return poem
