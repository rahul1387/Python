
# Continue
for i in range(12):
    if(i == 10):
        print("Skip the iteration")
        continue
    print("5 X", i, "=", 5*i)

# Break

i = 0
while True:
    print(i)
    i = i + 1
    if(i%100 == 0):
        break # ---> It will break the loop even if the condition of while is true.