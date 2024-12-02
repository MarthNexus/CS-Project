import time
from Catagorization import *
from JsonIO import *
from Math import *
file = 'dictonary.json'

io = json_IO(file)
dicton = io.dict_Get()

print("Welcome To the GPA maker!")
time.sleep(1)
print("We will calculate the GPA!")
time.sleep(1)
if dicton == {}:
    print("First we'll add your catagories!")
    intro()
    dicton = dictonary
else:
    print("Looks like you have a file! \nYou will be redirected to the main menu!")

math = cat_selection(dicton)


def main_menu(): 
    men_list = ['1:Enter Grade','2:GPA','3: Save','4: Quit']
    for menuing in range( len(men_list)):
        print(men_list[menuing])
    menuNo = int(input("Where would you like to start?: "))

    if menuNo == 1:
        math.get_Catagory()
        math.get_Average()
        return main_menu()
    if menuNo == 2:
        print("The program had calculated tour GPA! it is :",math.get_GPA())
        input('press enter to continue')
        return main_menu()

    if menuNo == 3:
        io.file_Update(dicton)
        print('File Save Succsess!')
        input('press enter to continue')
        return main_menu()
    if menuNo == 4:
        flag = input("Are you sure? Y or N")
        if flag == 'Y':
            exit
        if flag == 'N':
            return main_menu()

    
main_menu()
