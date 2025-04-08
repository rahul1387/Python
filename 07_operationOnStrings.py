fruit = "Mango"

# Length of string
mangoLen = len(fruit)
print(mangoLen)

# Print string letter by giving the ranges of indexes
print(fruit[0:4]) # including 0 but not 4 because it takes till n-1 limit

print(fruit[1:4]) # including 1 but not 4 
print(fruit[:5])
print(fruit[0:-3])
print(fruit[0:len(fruit)-3]) # python automatically minus the 3 by lenght of string.
print(fruit[-1:-3])
