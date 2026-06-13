#__init__() method
# is an instance method
# is used to crreate and initoalize the attribute during the object creation

class Student:
    """
    This is a class Student to manage student ifo and activities
    """

    def __init__(self,name,roll):
        print("Calling the initializer")
        self.name = name
        self.roll = roll

    def study(self,n_hours):
        print(f"Self is:{self}")  #o/p => self is: <__main__.Student object at memory address
        print(f"The student studies for {n_hours} hours a day!") #o/p => The student studies for 2 hours a day!

    def sports(self,sports_name):
        print(f"The student plays {sports_name}")
    