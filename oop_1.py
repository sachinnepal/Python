# class Waiter:
#     def __init__(self):
#         self.tables=[]
    
#     def take_order(self,table_number):
#         self.tables.append(table_number)

# Raj=Waiter()
# simran=Waiter()

# Raj.take_order(1)
# simran.take_order(2)

# Raj.tables=[4,5,6]
# simran.tables=[1,2]

# print(Raj.tables)
# print(simran.tables)

# Raj.take_order()
# simran.take_order()

# print(Raj.tables)
# print(simran.tables)



class staff:
    def __init__(self,name,shift):
        self.name=name
        self.shift=shift

    def start_work(self):
        print(f"{self.name} starts work on {self.shift} shift")
    def work(self):
        print(f"{self.name} is working")

class Waiter(staff):
    def take_order(self):
        print(f"{self.name } is taking order")
        
class Chef (staff):
    def cook_food(self):
        print(f"{self.name}is cooking food ")



raj=Waiter("Raj","Morning")
amit=Chef("Amit","Night")

print(raj.start_work())
print(amit.cook_food())


