myint = 7
print(myint)

myfloat = 7.0 #giving myfloat a value by simply using an absolute decimal value
print(myfloat)
myfloat = float(7) #giving myfloat a value using float() function, converting the number 7 into a decimal value
print(myfloat)

mystring = 'hello' #giving string a value using single quote
print(mystring) 
mystring = "hello" #giving string a value using double quote 
print (mystring)

# Simple operators can be executed on numbers and strings
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

#assignments can be done on more than 1 variable simultaneously on the same line
a, b = 3, 4
print(a, b)

#exercise
mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Int: %i" % myint)