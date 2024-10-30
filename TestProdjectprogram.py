import time
dictionary = {ammount_of_students : 0}
listOfGrade = []
student= []

def studentMenuStart():
    print("Entering student menu..")
    time.sleep(1)
    #still in test tying some dictionary probably
    input ""

def gradeMenu():
    print("in gradeMenu")
    insertedGrade = 0
    while insertedGrade != -1: 
        insertedGrade = int(input("Entering Grade\nPlease enter Grade: "))
        if insertedGrade < -1:
            raise Exception ("Sorry but negative numbers are invalid")
        elif insertedGrade > 100:
            raise Exception ("Sorry but we can't go over 100")
        listOfGrades.append(insertedGrade)


def averaging(averages):
    Average = sum(gradelist)/len(insertedgradelist) 

def 
def

