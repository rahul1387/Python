import time # ---> importing time library.

timestam = time.strftime("%H:%M:%S")
print(timestam)

if(timestam > "00" and timestam < "12"):
    print("Good Morning Sir")
elif(timestam > "12" and timestam < "17"):
    print("Goof Aftetnoon Sir")
elif(timestam > "17" and timestam < "20"):
    print("Good Evening Sir")
elif(timestam > "20" and timestam < "24"):
    print("Good Night Sir")
