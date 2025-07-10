a = 9
b = 9
if(a>b):
    print("First number is greater")
else:
    print("Second number is greater or equal")

# This is how we define a function in python.
# And the variables in bracket are called as arguments.
def ifGreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")

def isLesser(a,b):
    pass # ---> this means this function will be passed bcuz it has pass funcion in it which skips the function due to pending code.

def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)