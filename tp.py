def compare(a,b):
    ap = 0
    for i in a:
        for j in b:
            if i>j: ap+=1
    return ap

a = [5,6,7];
b = [3,6,10];
print(compare(a,b));