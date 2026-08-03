#Experiment with bool() on 0, 1, "", "AI", [], [1], and {} to see which values evaluate to True or False.
print(bool(0))  # False
print(bool(1))  # True
print(bool(""))  # False
print(bool("AI"))  # True
print(bool([]))  # False
print(bool([1]))  # True
print(bool({}))  # False