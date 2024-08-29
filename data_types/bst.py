
class TreeNode:
	def __init__(self, val, left,right):
		self.left=left 
		self.right=right
		self.val=val

class BST:
	def __init__(self):
		self.root = TreeNode(0, None,None)

	def insert(self,val):
		self._insert(self.root,val)

	def remove(self,val):
		self._remove(self.root,val)

	def printInOrder(self):
		nodesInOrder=[]
		self._printInOrder(self.root,nodesInOrder)
		print(nodesInOrder)

	def _insert(self, node, val):
		if not node:
			return TreeNode(val,None,None)
		if val>node.val:
			node.right = self._insert(node.right,val)
		elif val<node.val:
			node.left = self._insert(node.left,val)
		return node 

	def _remove(self,node,val):
		if val>node.val:
			node.right = self._remove(node.right,val)
		elif val<node.val:
			node.left = self._remove(node.left,val) 
		else:
			if not node.left:
				return node.right
			elif not node.right:
				return node.left
			else:
				minNode = self._findMin(node.right)
				minNode.right = node.right
				node.right = self._remove(node.right,minNode.val)
		return node

	def _printInOrder(self,node,nodeValues):
		if not node:
			return

		self._printInOrder(node.left,nodeValues)
		if node.val == self.root.val:
			nodeValues.append(f"root:{node.val}")
		else:
			nodeValues.append(node.val)
		self._printInOrder(node.right,nodeValues)

	def _findMin(self,node):
		curr = node
		while curr and curr.left:
			curr = curr.left
		return curr

	def _findMax(self,node):
		curr = node
		while curr and curr.right:
			curr = curr.right
		return curr

	def _balance(self):
		minRight = self._findMin(self.root.right)
		maxLeft = self._findMax(self.root.left)
		self._remove(self.root, 1)
		newNode=TreeNode(1,self.root.left,self.root.right)
		self.root=newNode
		



bst = BST()
bst.insert(1)

bst.insert(-1)


bst.insert(2)
bst.printInOrder()

bst.insert(14)
bst.insert(5)
bst.remove(14)
bst.printInOrder()

bst._balance()
bst.printInOrder()




