class Student:
    pass
#Usually the attributes are defined inside the method class
student1 = Student()
student2 = Student()

#Attributes are defined as with dot notations
student1.name = "John"
student1.roll = 101
# INSTANCE VARIABLES {these are variables associated with object not class}=> name and roll
#2 att => name and roll
print(student1.name)
print(student1.roll)
#o/p => John and 101
print(student2.name)
print(student2.roll)
#o/p => 'Student' object has no attribue 'name'
print(student1.__dict__)
#o/p => {'name': 'John', 'roll': 101}
