dictonary = {'number_catagory': 2}
percentage = 0
percentages= []
catagories = []
# so the counter for number isnt running correctly i will ignow number = number - 1
def function (percentage,percentages):

    for number in range (dictonary ["number_catagory"]):
        word = input ('insert the catagory that you choose: ')  
        if word is None or word == '':
            print("sorry this must be filled ")
            number = number - 1
            continue 
        else:
            try:
                percentage = int(input ("what is the percentage of the catagory "))
        
            except TypeError:
                print ("must be a number")
                continue
        
            if percentage is None or percentage == '':
                print("sorry this must be filled ")
                number = number - 1
                continue

            else:
                percentages.append (percentage)
                catagories.append (word)

function(percentage,percentages)

if sum(percentages) != int(100):
    percentages.clear
    catagories.clear
    print (" Sorry these percentages do not make 100 ")
    function(percentage,percentages)
else:
    for lists in range(len(catagories)):
        dictonary [catagories [lists]] = percentages [lists]
print(dictonary)
