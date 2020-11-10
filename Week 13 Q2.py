def preorder(string):
    for i in range (0,n):
        print ("{}_".format(string[i]),end="")
        
def postorder(string):
    for l in range (0,n,2):
        print ("{}_".format(string[l]),end="")
    for q in range (n-1,0,-2):
        print ("{}_".format(string[q]),end="")  
        
def inorder(string):
    s = string
    s.sort()
    for i in range (0,n):
        print ("{}_".format(s[i]),end="")


n = int (input())
string = input().split(" ")
preorder(string)
print()
inorder(string)
print()
postorder(string)
