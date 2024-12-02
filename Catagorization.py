dictonary = {}
percentage = 0
percentages= []
catagories = []


def function(percentage,percentages):

    while percentage != None :
        
        if dictonary['number_catagory'] == len(percentages) :
            return validation()
        
        word = input ('insert the catagory that you choose: ')  

        if word is None or word == '':
            print("sorry this must be filled ")
            continue 

        else:
            try:
                percentage = int(input ("what is the percentage of the catagory "))
            except (TypeError, ValueError)as e :
                print (e,"must be a number")
                continue
            
        
            if percentage is None or percentage == '':
                print("sorry this must be filled ")
                continue
            
            else:
                percentages.append (percentage)
                catagories.append (word)
                
def validation():

    if sum(percentages) != int(100):
        percentages.clear()
        catagories.clear()
        print (" Sorry these percentages do not make 100 ")

        return function(percentage,percentages)
    
    else:
        for lists in range(len(catagories)):
            dictonary [catagories [lists]] = percentages [lists]


def intro():
    while percentage != "":
        try:
            numb_catagories = int(input("enter the number of categories: "))
        except ValueError:
            print ("sorry only numbers")
            continue
        break
    dictonary ['number_catagory'] = int(numb_catagories)
    return function(percentage,percentages)

