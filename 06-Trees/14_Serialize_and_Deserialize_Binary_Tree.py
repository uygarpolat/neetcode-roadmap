"""
Serialize and Deserialize Binary Tree

https://neetcode.io/problems/serialize-and-deserialize-binary-tree?list=neetcode150

Implement an algorithm to serialize and deserialize a binary tree.

Serialization is the process of converting an in-memory structure into a sequence of bits so that it can be stored or sent across a network to be reconstructed later in another computer environment.

You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure. There is no additional restriction on how your serialization/deserialization algorithm should work.

Note: The input/output format in the examples is the same as how NeetCode serializes a binary tree. You do not necessarily need to follow this format.

Example 1:

Input: root = [1,2,3,null,null,4,5]

Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []

Output: []
Constraints:

0 <= The number of nodes in the tree <= 1000.
-1000 <= Node.val <= 1000
"""
from typing import Optional
from collections import deque

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Codec:
    
	def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
		def check_trees(node1, node2):
			if node1 == None or node2 == None:
				if node1 != node2:
					return False
				return True
			if node1.val != node2.val:
				return False
			return check_trees(node1.left, node2.left) and check_trees(node1.right, node2.right)
		return check_trees(p, q)
	
	def serialize(self, root: Optional[TreeNode]) -> str:
		result = []
		queue = deque([root])

		while queue:
			length = len(queue)
			for _ in range(length):
				local = queue.popleft()
				if local:
					result.append(str(local.val))
					queue.append(local.left)
					queue.append(local.right)
				else:
					result.append("N")
		return ",".join(result).rstrip(",N")

	def deserialize(self, data: str) -> Optional[TreeNode]:

		if not data or data[0] == "N":
			return None

		data_lst = data.split(',')

		length = len(data_lst)
		root = TreeNode(int(data_lst[0]))
		queue = deque([root])
		index = 1

		while queue and index < length:
			node = queue.popleft()
			if index < length and data_lst[index] != "N":
				node.left = TreeNode(int(data_lst[index]))
				queue.append(node.left)
			index += 1
			if index < length and data_lst[index] != "N":
				node.right = TreeNode(int(data_lst[index]))
				queue.append(node.right)
			index += 1
		return root

def main():
	codec = Codec()

	root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
	str = codec.serialize(root)
	deserialized_root = codec.deserialize(str)
	assert codec.isSameTree(root, deserialized_root) == True

	root = TreeNode()
	str = codec.serialize(root)
	deserialized_root = codec.deserialize(str)
	assert codec.isSameTree(root, deserialized_root) == True
	
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
