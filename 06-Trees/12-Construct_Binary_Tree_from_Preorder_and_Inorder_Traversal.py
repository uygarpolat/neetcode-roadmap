"""
Construct Binary Tree from Preorder and Inorder Traversal

https://neetcode.io/problems/binary-tree-from-preorder-and-inorder-traversal?list=neetcode150

You are given two integer arrays preorder and inorder.

preorder is the preorder traversal of a binary tree
inorder is the inorder traversal of the same tree
Both arrays are of the same size and consist of unique values.
Rebuild the binary tree from the preorder and inorder traversals and return its root.

Example 1:

Input: preorder = [1,2,3,4], inorder = [2,1,3,4]

Output: [1,2,3,null,null,null,4]
Example 2:

Input: preorder = [1], inorder = [1]

Output: [1]
Constraints:

1 <= inorder.length <= 1000.
inorder.length == preorder.length
-1000 <= preorder[i], inorder[i] <= 1000
"""
from typing import List, Optional

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
		
		tally = {}
		for index, value in enumerate(inorder):
			tally[value] = index
        
		global_index = 0
		def traverse(l, r):
			if l > r:
				return None

			nonlocal global_index
			root_val = preorder[global_index]
			global_index += 1
			root = TreeNode(root_val)
			mid = tally[root_val]
			root.left = traverse(l, mid - 1)
			root.right = traverse(mid + 1, r)
			return root

		return traverse(0, len(inorder) - 1)
