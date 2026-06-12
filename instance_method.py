#Instance Method
#define inside the class which is bound to/ associated with the instance/object

#help(list)

class Student:
    """
    This is a class Student o manage student info and activities
    """

    def study():
        return "The student studies for 2 hours a day!"
    
student1 = Student()
print(student1) #o/p => <__main__.Student object at 0x0000232831> = memory space

student1.study() #o/p => TypeError: Student.study() takes 0 positional arg but 1 was given
#Here 1 means not explicitly given but represents the internal function call of method 

def greet():
    print("Hello there!")

greet()
#o/p => Hello there!
greet("Python")
#o/p => TypeError: greet() takes 0 position arg but 1 was given

class Student:
    """
    This is a class Student o manage student info and activities
    """

    def study(self):
        print(f"Self is:{self}")  #o/p => self is: <__main__.Student object at memory address
        print("The student studies for 2 hours a day!") #o/p => The student studies for 2 hours a day!
    
student1 = Student()
print(f"The object:{student1}")
#o/p => The object: <__main__.Student object at memory address>

student1.study() #Here student1 = object and study = function


"""
When we call an instance method using the object/instance of the class, Python passes the object itself
as the first  arg to that method
So the first arg of any instance method is the object itself
That first argument is by standard is self
"""

