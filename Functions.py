#Functions in python are defined using the block keyword "def", followed with the function's name as the block's name. 
def my_function():
    print("Hello From my function!")

#Functions may also receive arguments (variables passed from the caller to the function).
def my_function_with_args(username, greeting):
    print("Hello, %s , from my function, I wish you %s" %(username, greeting))

#Functions may return a value to the caller, using the keyword- 'return'
def sum_two_numbers(a, b):
    return a + b



#to call a function Simply write the function's name followed by (), placing any required arguments within the brackets.
def my_function():
    print("Hello from my function!")

def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b
my_function()
my_function_with_args("John Doe", "a great year!")
x = sum_two_numbers(1,2)

#exercise
def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()