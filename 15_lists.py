marks = [3,6,9,"Mango"];
print(marks)
print(type(marks))
print(marks[0]) # ---> Accessing the element of that list using index.
print(marks[1])
print(marks[2])

print(marks[-3]) #Negative index.
print(marks[len(marks)-3]) #Positive index
print(marks[5-4]) #POsitive index

if "6" in marks:
    print("Yes")
else:
    print("No")

# Same thing applies for strings as well!
# if "Ha" in "Harry":
#   print("Yes")

# print(marks[0:7])
# print(marks[1:9])
# print(marks[1:9:3])

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)
