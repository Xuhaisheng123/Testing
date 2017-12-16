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
	
	def insert(self,label1):
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
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	