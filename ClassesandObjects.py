#a very basic class would look something like this:
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside a class")


#We'll explain why you have to include that "self" as a parameter a little bit later. First, to assign the above class(template) to an object you would do the following:
myobjectx = MyClass()

#To access the variable inside of the newly created object "myobjectx" you would do the following:
myobjectx.variable

#So for instance the below would output the string "blah":
print(myobjectx.variable)

#You can create multiple different objects that are of the same class(have the same variables and functions defined). However, each object contains independent copies of the variables defined in the class. For instance, if we were to define another object with the "MyClass" class and then change the string in the variable above:
myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

print(myobjectx.variable)
print(myobjecty.variable)

#To access a function inside of an object you use notation similar to accessing a variable:
myobjectx.function()

#The __init__() function, is a special function that is called when the class is being initiated. It's used for assigning values in a class.
class NumberHolder:
    def __init__(self, number):
        self.number = number


#exercise
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
    
car1 = Vehicle()
car1.name = "Fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.kind = "van"
car2.color = "blue"
car2.value = 10000.00

print(car1.description())
print(car2.description())
