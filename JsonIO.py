import json

class json_IO():
    def __init__ (self, file_name):
        try:
            self.name = file_name
            self.fiOp = open(self.name,'r')
            self.file = json.load(self.fiOp)
            self.fiOp.close()
            

        except FileNotFoundError:
            def file_Create(self):  
                yorn = input("File Not Found!!\nDo you want to make one? Y or N: ")
                if yorn == 'Y':
                    self.fiOp = open(self.name,'w')
                    self.file = {}
                    json.dump(self.file,self.fiOp,indent=4)
                    self.fiOp.close()
                    
                elif yorn == 'N':
                    print("--Saving Disabled-- \n[ALL WORK WILL NOT BE SAVED UPON CLOSING]")
                    self.file = {}
                else:
                    return file_Create()
            file_Create(self)

    def dict_Get(self):
        return self.file


    def file_Update(self,dictionary):
        self.fiOp = open(self.name,"r+")
        self.file = dictionary
        self.fiOp.seek(0)
        self.fiOp.truncate()
        json.dump(self.file,self.fiOp,indent=4)
        self.fiOp.close()
    


            
            

