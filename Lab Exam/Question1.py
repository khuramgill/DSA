import pandas as pd
import random

class Student:
    def __init__(self, Rollno,Name,Marks):
        self.Rollno = Rollno
        self.Name = Name
        self.Marks = Marks

    def randomStudentData(self,n):
        Rollno = [i for i in range(1,n+1)]
        Name = ['Student'+str(i) for i in range(1,n+1)]
        Marks = [random.randint(0,100) for i in range(1,n+1)]
        df = pd.DataFrame(list(zip(Rollno,Name,Marks)),columns = ['Rollno','Name','Marks'])
        return df
    def plot(self,x,y,kind):
        df = pd.DataFrame(list(zip(self.Rollno,self.Marks)),columns = [x,y])
        df.plot(x=x,y=y,kind=kind)

    def BubbleSort(self):
        for i in range(len(self.Marks)):
            print("k")
            for j in range(len(self.Marks)-i-1):
                if self.Marks[j] > self.Marks[j+1]:
                    self.Marks[j],self.Marks[j+1] = self.Marks[j+1],self.Marks[j]
                    self.Rollno[j],self.Rollno[j+1] = self.Rollno[j+1],self.Rollno[j]
                    self.Name[j],self.Name[j+1] = self.Name[j+1],self.Name[j]
                    self.storeincsv(self)
        return self.Rollno,self.Name,self.Marks
    
    def plotBubbleSort(self):
        df = pd.DataFrame(list(zip(self.Rollno,self.Marks)),columns = ['Rollno','Marks'])
        df.plot(x='Rollno',y='Marks',kind='line')
    def storeincsv(self):
        df = pd.DataFrame(list(zip(self.Rollno,self.Marks)),columns = ['Rollno','Marks'])
        df.to_csv('BubbleSort.csv',index=False)
    

if __name__ == '__main__':
    std = Student()
    std = std.randomStudentData(100)
    print(std)
    std.plot(x='Rollno',y='Marks',kind='line')
    std.BubbleSort()
    
 