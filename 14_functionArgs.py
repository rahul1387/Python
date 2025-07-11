def average(a, b, c=1): # ---> inside bracket all var are called as arguments and we can give value inside the bracket too 
    print("The average is " , (a + b + c)/3)

average(2,3)

def avg(*numbers):
    # print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is: " , sum / len(numbers))

avg(2 , 4)