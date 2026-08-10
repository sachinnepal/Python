class car:
    category="4 wheeler" #class attribute

    def __init__(self,color,brand):
      self.color=color      #object attribute
      self.brand=brand      #object attribute (High Prority)

    def welcome(self):
        print("WELCOME TO THE ")

car1=car("Green","Toyata")
print(car1.color,car1.brand,car1.category)

car2=car("White","Toyata")
print(car2.color,car2.brand,car2.category)

car2.welcome()

    

