'''
A binary search tree
'''

class Node:
	
	def __init__(self,label,parent):
		self.label = label
		self.parent = parent
		self.left = None
		self.right = None 
		
	def getLabel(self):
		return self.label
	
	def setLabel(self,label1):
		self.label = label1
		
	def getLeft(self):
		return self.left
		
	def setLeft(self,left):
		self.left = left
	
	def getRight(self):
		return self.right
		
	def setRight(self,right):
		self.right = right
		
	def getParent(self):
		return self.parent
	
	def setParent(self,parent):
		self.parent = parent
		
class BinarySearchTree:
	
	def __init__(self):
		self.root = None
	
	def insert(self,label):
		#Create a new node
		new_node = Node(label,None)
		#If tree is empty
		if self.empty():
			self.root = new_node
		else:
			#If tree is not empty
			curr_node = self.root
			#while we don't get to a leaf
			while curr_node is not None:
				#we keep reference of the parent node 
				parent_node = curr_node
				#If node label is less than current node 
				if new_node.getLabel() < curr_node.getLabel():
					#we go left
					curr_node = curr_node.getLeft()
				else:
					#else we go right
					cuur_node = curr_node.getRight()
			#we insert the new node in a leaf
			if new_node.getLabel() < parent_node.getLabel():
				parent_node.setLeft(new_node)
			else:
				parent_node.setRight(new_node)
			#set parent to the new node
			new_node.setParent(parent_node)
	
	
	def delete(self,label):
		if(not self.empty()):
			 #look for the node with  that label
			 node = self.getNode(label)
			 #if the node exists
			 if (node is not None):
				#if the node has no child
				if (node .getLeft() is None and node.getRight() is None ):
					self.__reassignNodes(node,None)
					node = None
				#Only has right child
				elif （node.getLeft() is None and node.getRight() is not None）:
					self.__reassignNodes(node,node.getRight())
				#Has only left children
				elif (node.getLeft() is not None and node.getRight() is None):
					self.__reassignNodes(node ,node.getLeft())
				#Has two children
				else:
					#Gets the max value of the left brach
					tmpNode = self.getMax(node.getLeft())
					#Delete the tmpNode
					self.delete(tmpNode.getLeft())
					#Assigns the value to the node to delete and keeps tree structure
					node.setLabel(tmpNode.getLabel())
	
	
	def getNode(self,label):
		curr_node = None
		#If the tree is not empty
		if(not self.empty()):
			#Get tree root
			curr_node = self.getRoot()
			#while we don't find the node wo looking for
			#I am using lazy evaluation here to avoid NoneType Attribute error
			while curr_node is not None and curr_node.getLabel() is not label:
				#If node label less than curr_node label we go left				
				if curr_node.getLabel() > label:
					curr_node = curr_node.getLeft()
				else: 
					curr_node = curr_node.getRight()
					
			return curr_node
	
	
	def getMax(self,root = None):
		if (root is not None):
			curr_node = root
		else:
			#we go deep to the right branch
			curr_node = self.getRoot()
		if (not self.empty()):
			while (curr_node.getRight() is not None):
				curr_node = curr_node.getRight()
		return curr_node
	
	def getMin(self,root = None):
		if (root is not None):
			curr_node = root
		else:
			curr_node = self.getRoot()
			
		if (not self.empty()):
			while (curr_node.getLeft() is not None):
				curr_node  = curr_node.getLeft()
		return curr_node
	#function empty :judge if the tree is a empty tree  
	def empty(self):
		if self.root is None:
			return True
		else:
			return False
	
	#Traverse the tree,stored in the nodeList
	def __InOrderTraversal(self,curr_node):
		nodeList = []
		if curr_node is not None :
			nodeList.insert(0,curr_node)
			nodeList = nodeList + self.__InOrderTraversal(curr_node.getLeft())
			nodeList = nodeList + self.__InOrderTraversal(curr_node.getRight())
		return nodeList
	
	def getRoot(self):
		return self.root
		
	def __isRightChildren(self,node):
		if(node == node.getParent().getRight()):
			return True
		return False
		
	def __reassignNodes(self,node,newChildren):
		if(newChildren is not None):
			newChildren.setParent(node.getParent)
		
		if (node.getParent() is not None):
			#if it is the right Children
			if(slef.__isRightChildren(node)):
				node.getParent().setRight(newChildren)
			else:
				#Else it is the left children
				node.getParent().setLeft(newChildren)
	
	#This function traversal the tree. By default it returns an
	#In order traversal list. You can pass a function to traversal
    #The tree as needed by client code
	def traversalTree(self,traversalFunction = None,root = None):
		if(traversalFunction is None):
			#Return a list of nodes in preOrder by default
			return self.__InOrderTraversal(self.root)
		else:
			#Return a list of node in the order that the users wants to
			return traversalFunction(self.root)
			
	#Returns an string of all the nodes labels in the list 
    #In Order Traversal
	def __str__(self):
		list = self.__InOrderTraversal(self.root)
		str = ""
		for x in list:
			str = str + " " + x.getLabel().__str__()
		return str
	def InPreOrder(curr_node):
		nodeList = []
		if curr_node is not None:
			nodeList = nodeList + InPreOrder(curr_node.getLeft())
			nodeList.insert(0,curr_node.getLabel())
			nodeList = nodeList + InPreOrder(curr_node.getRight())
		return nodeList
	
##testing	
		
	
	
	
	
	
	
