n = int (input("enter the value: "))
for i in range (1, n + 1):
    a = 0
    for j in range (2, i):
        if(i%j == 0):
           a = 1
           break
    if (a == 0):
        print(i, end = ' ')
