# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
  #Enter your code here
    while(root != None):
        if(v1 > root.info and v2 > root.info):
            root = root.right
        elif(v1 < root.info and v2 < root.info):
            root = root.left
        else:
            break
    return root
