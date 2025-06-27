"""
Same Binary Tree

https://neetcode.io/problems/same-binary-tree?list=neetcode150

Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

Example 1:

Input: p = [1,2,3], q = [1,2,3]

Output: true
Example 2:

Input: p = [4,7], q = [4,null,7]

Output: false
Example 3:

Input: p = [1,2,3], q = [1,3,2]

Output: false
Constraints:

0 <= The number of nodes in both trees <= 100.
-100 <= Node.val <= 100
"""
from typing import Optional

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
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
