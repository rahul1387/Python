def checkTranspose(a):
    for i in range(len(a)):
        for j in range(len(a)):
            print(a[i][j],end=' ')
        print()
a = [[1,2,3],[4,5,6],[7,8,9]]

checkTranspose(a)