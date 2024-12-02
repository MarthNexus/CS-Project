from Catagorization import *

class cat_selection():
    def __init__(self,dictionary):
        self.dict = dictionary
        self.catagory = dictionary
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

        try:
            print(self.fin)
            cat = int(input("Choose a catagory   : "))
        except TypeError:
            print("Only numbers!")
            return get_Catagory()
        

        self.usedcat = self.fin[cat - 1]
        
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
            grade.append(self.table ['Grades'][self.fin[gweid]])
            weight.append(self.table ['Averages'][self.fin[gweid]])

        for count in range(len(grade)):
            gpa_weighted.append(int(grade[count])*int(weight[count]))

        per = int(sum(gpa_weighted))/100
        gpa = round(4.00 * per,2)
        return gpa

        
    def get_Average(self):
        #average for single
        average = sum(self.table['Grades'][self.usedcat])/len(self.table['Grades'][self.usedcat])
        self.table['Averages'][self.usedcat] = average
