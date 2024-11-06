dict = {}
#we want to use this to be able to store how many categories their weights and what the category is 
numb_categories = 0
while numb_categories != "":
    try:
        numb_catagories = int(input("enter the number of categories: "))
    except ValueError:
        print ("sorry only numbers")
        continue
    break
dict ["categories"] = int(numb_catagories)
print (dict)


