x = 2
print(x == 2)
print(x == 3)
print(x < 3)

#The "and" and "or" boolean operators allow building complex boolean expressions
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John and you are 23 years old")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick")

#The "in" operator could be used to check if a specified object exists within an iterable object container
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick")

#is operator
#Unlike the double equals operator "==", the "is" operator does not match the values of the variables, but the instances themselves. 
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

#not operator
#Using "not" before a boolean expression inverts it:

print(not False)
print(not not True)

#excerise 
number = 20
second_number = 0
first_array = [1, 2, 3]
second_array = [1, 2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")
