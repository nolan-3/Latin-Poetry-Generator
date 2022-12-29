from higherLower import popularity
import random
table = popularity.table

def randomPair():
    first = table[random.randint(1,997)]
    second = table[random.randint(1,997)]
    while first == second:
            second = table[random.randint(1,997)]
    return [first, second]

def check(guess, option1, option2):
    print("check is called")
    if not guess:
        print("guess is null")
        return randomPair()
    if not option1:
        print("option 1 is None")
        return randomPair()
    if not option2:
        print("option2 is null")
        return randomPair()


    if(option1[1] > option2[1]):
        correct = 'lower'
    elif(option1[1] < option2[1]):
        correct = 'higher'
    print("guess is " + guess)
    print("correct is " + correct)
    if guess == correct:
        newOption = table[random.randint(1,997)]
        while newOption == option2:
            newOption = table[random.randint(1,997)]
    return [True, newOption, option1]
