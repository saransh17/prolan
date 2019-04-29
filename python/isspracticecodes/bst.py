class node:
	def __init__(self,value):
		self.value = value
		self.right = None
		self.left  = None

def insert(root,node):
	if root is None :
		root = node
	else :
		if  root.value > node.value : 
			if root.left is None :
				root.left = node
			else:
				insert(root.left , node)
		else :
			if root.right is None :
				root.right = node
			else:
				insert(root.right , node)

def inorder(root):
	if root :
		inorder(root.left)
		print(root.value)
		inorder(root.right)

n = int(input("Enter the number of nodes : "))
val = int(input("Enter the value : "))
r = node(val)
for i in range(1,n): 
	val = int(input("Enter the value : "))
	insert(r,node(val)) 

inorder(r)