from data import table
from translations import translations
import random
import string

# replaces letters not included in the lookup table: j, u, y


def checkLetter(letter):
    if letter.isalpha():
        if letter == 'j':
            letter = 'i'
        elif letter == 'u':
            letter = 'v'
        elif letter == 'y':
            letter = 'z'
    else:
        letter = ''
    return letter


def generate(message):
    # stores which half line was used for each selection
    chosenLetters = []
    message = message.lower().strip()
    poem = ''
    translation = ''
    endOfLine = False
    # current index in the string (only counting letters)
    charNum = 0
    # number of dictionaries in the lookup table
    numOfDicts = len(table)


    # eliminate letters not included in the table
    tempString = ''
    for i in range(0, len(message)):
        tempString += checkLetter(message[i])
    message = tempString

    #make sure the poem has a full last line
    if(len(message) % 2 == 1):
        char = random.choice(string.ascii_letters).lower()
        char = checkLetter(char)
        message += char

    for i in range(0, len(message)):
        # add letters from message to chosenLetters
        if(i % 2 == 0):
            chosenLetters.append([message[i],message[i+1]])
        char = message[i]
        # if message length > number of dictionaries, recycle them
        dictNum = charNum % numOfDicts
        # isalpha() isn't necessary but its a nice tool to have
        # UPDATE none of this should be necessasry, all handled in cleansing message
        if char.isalpha() and ord(char) >= 97 and ord(char) <= 122:

            halfLine = table[dictNum][char][0]
            halfEng = table[dictNum][char][1]
            # add a new line if at the end of a line of latin
            if (endOfLine):
                poem += halfLine + '\n'
                endOfLine = False
            else:
                poem += halfLine + ' '
                endOfLine = True
            charNum += 1

    # translate poem
    for i in range(0,len(chosenLetters)):
        firstLetter = chosenLetters[i][0]
        secondLetter = chosenLetters[i][1]
        index = i % 8
        line = translations[index][firstLetter][secondLetter]
        translation += line + '\n'

    return [poem, translation]
