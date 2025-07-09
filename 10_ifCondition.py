age = int( input("Enter your age: "))

#If-Else 
if(age>=18):
    print("You can drive!")
else:
    print("You cannot drive")


applePrice = int(input("Enter the apple price: "))
budget = int(input("Enter your budget: "))

# elif ladder
    
if(budget - applePrice > 50):
        print("Alexa, add 1kg apples to the card.")
elif(budget - applePrice > 70):
        print("Its okay you can buy ")
else:
        print("Alexa, do not add apples to the card.")
