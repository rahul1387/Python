a = "1";
b = "2";

print(a + b);

''' A convertion of one data type into another data type is known as Type Casting.
 There are various functions or methods like int(), float(), str(),ord(),list(),dict(),hex(), etc.
Tow types of typecasting :  1.Explict typeCasting (Applied by programmer)
                            2.Implict typeCasting (Applied by Python)
'''       
# Explict typeCasting                     
print(int(a) + int(b));  # but if we add any letters in a or b and tell it to add then the error will occur and here we have converted aur string data to integer with using int function.

# Implict Typecasting
num1 = 2;
num2 = 3.3;

print(num1 + num2);