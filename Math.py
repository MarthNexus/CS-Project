from Catagorization import *

class cat_selection():
    def __init__(self,dictionary):
        self.dict = dictionary
        self.catagory = dictionary
        print(self.catagory)
        del self.catagory['number_catagory']
        self.fin = list(self.catagory.keys())
        self.table = {}
        self.table ['Grades']={}
        self.table ['Averages']={}
        for tab in range(len(self.fin)):
            self.table ['Grades'][self.fin[tab]] = []
            self.table ['Averages'][self.fin[tab]] = 0

    def get_Catagory(self):
        flag = False
        while flag != True:
            try:
                print(self.fin)
                cat = int(input("Choose a catagory   : "))
            except ValueError:
                print("Only numbers!")
                continue
        
            try:
                self.usedcat = self.fin[cat - 1]
            except IndexError:
                print("Out of Range!!")
                continue
            flag = True
        flag = False
        
        while flag != True:
            try:
                grade = int(input("List your grade here: "))
            except TypeError:
                print("Only Numbers!!")
                continue


            self.table ['Grades'][self.usedcat].append(int(grade))
            
            flag = input("do you want to stop? Y or N :")
            if flag == "Y":
                flag = True
        flag = False

    def get_GPA(self):
        
        grade = []
        weight = []
        gpa_weighted = []

        for gweid in range(len(self.fin)):
            grade.append(self.table ['Averages'][self.fin[gweid]])
            weight.append(self.dict [self.fin[gweid]]/100)

        for count in range(len(grade)):
            gpa_weighted.append((grade[count])*(weight[count]))
            
        per = int(sum(gpa_weighted))
        gpa = round(4.00 * (per/100),2)
        return gpa

        
    def get_Average(self):
        #average for single
        average = int(sum(self.table['Grades'][self.usedcat])/len(self.table['Grades'][self.usedcat]))
        self.table['Averages'][self.usedcat] = average
