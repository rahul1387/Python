name = "Rahul" # String can be defined in double or single coats. 
print("Hello", name)

# The following pattern is to print string inside a string  
a = 'He said, "I will be playing football"'
print(a)

# Multi lines string
b = """I want eat apple
       I want to play online games
       Hey, how are you?
    """ # So in this way we can write string in multiple lines by using triple coat.
 
# Indexing in strings   
print(name[0]) # ---> This will print first letter of name which is 'R'.The indexing in programming starts from 0 to limit of string.   
print(name[1]) # ---> 'a'
print(name[2]) # ---> 'h' 
print(name[3]) # ---> 'u'
print(name[4]) # ---> 'l'
# print(name[5])  ---> This will throw an error because there is nothing on 5th index,its empty 

# The above proccess is very long tu print each element of string, if the string contains large number of elements.

# We use simplest process to print too many elements of string at once by using string-for loop. following is the syntax of it

for character in b:
    print(character) 
# The character contains each elements of b. And we can get all elements of a string in just two lines doesn't matter how many elements are there. 
