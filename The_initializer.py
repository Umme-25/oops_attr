#__init__() method
# is an instance method
# is used to crreate and initoalize the attribute during the object creation

class Student:
    """
    This is a class Student to manage student ifo and activities
    """

    def __init__(self,name,roll,dept):
        print("Calling the initializer")
        self.name = name
        self.roll = roll
        self.department = dept

    def study(self,n_hours):
        print(f"Self is:{self}")  #o/p => self is: <__main__.Student object at memory address
        print(f"The student studies for {n_hours} hours a day!") #o/p => The student studies for 2 hours a day!

    def sports(self,sports_name):
        print(f"The student plays {sports_name}")
    
student1 = Student("John",1001,"Science")

student2 = Student("Carol",1002,"Arts")

print(student1.name,student1.roll,student1.department)
print(student2.name,student2.roll,student2.department)

print(student1.__dict__)
print(student2.__dict__)

"""
Instance variable/attribute are different for different objects
"""
