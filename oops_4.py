class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    #static methods
    @staticmethod
    def static_methods():
        print("DEMO OF STATIC METHODS")
    
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+= val
        print(self.name,"Marks:",sum/3)


s1=Student("Sachin Nepal",[99,98,97])
s1.get_avg()
s1.static_methods()




