from newFile import table
# letters not included in the lookup table: j, u, y
def generate(message):
    message = message.lower().strip()
    poem = ''
    endOfLine = False
    #current index in the string (only counting letters)
    charNum = 0
    #number of dictionaries in the lookup table
    numOfDicts = len(table)

    #eliminate letters not included in the table
    tempString = ''
    for i in range(0, len(message)):
        if message[i] == 'j':
            tempString += 'i'
        elif message[i] == 'u':
            tempString += 'v'
        elif message[i] == 'y':
            tempString += 'z'
        else:
            tempString += message[i]
    message = tempString


    for i in range(0, len(message)):
        char = message[i]
        #if message length > number of dictionaries, recycle them
        dictNum = charNum % numOfDicts
        #isalpha() isn't necessary but its a nice tool to have
        if char.isalpha() and ord(char) >= 97 and ord(char) <= 122:
            halfLine = table[dictNum][char]
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
    print(poem)
    return poem
