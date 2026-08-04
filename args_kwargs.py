

 #*args and **kwargs are used to pass a variable number of arguments to a function. 
# def add(*args):
#     print(args[0] + args[1]+ args[2]+args[3]+args[4])

# add(1,2,3,4,5)

# def add2(*args):
#     print(sum(args))

# add2(1, 2, 3, 4, 5)
# add2(10, 20)
# add2(1, 2, 3, 4, 5, 6, 7)


# def student(**kwargs):
#     print(kwargs)

# student(name="Sachin", age=21, country="Nepal")
def demo(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

demo(1, 2, 3, name="Sachin", age=21)