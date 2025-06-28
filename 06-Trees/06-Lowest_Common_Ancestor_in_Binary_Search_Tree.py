"""
Lowest Common Ancestor in Binary Search Tree

https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree?list=neetcode150

Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.

The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants. The ancestor is allowed to be a descendant of itself.

Example 1:

Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8

Output: 5
Example 2:

Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4

Output: 3
Explanation: The LCA of nodes 3 and 4 is 3, since a node can be a descendant of itself.

Constraints:

2 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100
p != q
p and q will both exist in the BST.
"""
from typing import Optional

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
		val_p = p.val
		val_q = q.val
		def traverse_bst(node: TreeNode) -> TreeNode:
			if node == None:
				return None
			if node.val == val_p or node.val == val_q:
				return node
			
			if val_p < node.val and val_q < node.val:
				return traverse_bst(node.left)
			elif val_p > node.val and val_q > node.val:
				return traverse_bst(node.right)
			else:
				return node

		return traverse_bst(root)
