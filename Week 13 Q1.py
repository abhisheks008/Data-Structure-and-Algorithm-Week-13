n = int(input())
x_i = input().split(" ")
k = int(input())
count = 0
y_i = input().split(" ")
for i in range (0,k):
    for j in range (0,n):
        if (int(y_i[i])==int(x_i[j])):
            print ("y")
            break
        else :
            count = count + 1
    if (count==n-1):
        print ("n")
