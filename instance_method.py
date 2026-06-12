#Instance Method
#define inside the class which is bound to/ associated with the instance/object

#help(list)

class Student:
    """
    This is a class Student o manage student info and activities
    """

    def study():
        return "The student studies for 2 hours a dday!"
    
student1 = Student()
print(student1) #o/p => <__main__.Student object at 0x0000232831> = memory space

student1.study() #o/p => TypeError: Student.study() takes 0 positional arg but 1 was given


def greet():
    print("Hello there!")

greet()
#o/p => Hello there!
greet("Python")
#o/p => TypeError: greet() takes 0 position arg but 1 was given
