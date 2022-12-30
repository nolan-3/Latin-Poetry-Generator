from higherLower import popularity
import random

# I should be able to remove these from the table then right?
table = popularity.table

class whyNecessary:
    tableLen = 997

obj = whyNecessary()

def randomOption():
    rand = random.randint(1,obj.tableLen)
    option = table[rand]
    #make sure we don't choose the same option again this game
    del table[rand]
    obj.tableLen -= 1
    return option

def check(guess, option1, option2):

    #print("check is called")
    # the only time this should happen is when all 3 are null from a GET request
    if not guess:
        #print("guess is null")
        return [randomOption(), randomOption()]
    if not option1:
        #print("option 1 is None")
        return [randomOption(), randomOption()]
    if not option2:
        #print("option2 is null")
        return [randomOption(), randomOption()]


    if(option1[1] > option2[1]):
        correct = 'lower'
    elif(option1[1] < option2[1]):
        correct = 'higher'

    print("guess is " + guess)
    print("correct is " + correct)

    if guess == correct:
        return True
    else:
        return False
