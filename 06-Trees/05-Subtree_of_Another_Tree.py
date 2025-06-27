"""
Subtree of Another Tree

https://neetcode.io/problems/subtree-of-a-binary-tree?list=neetcode150

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:

Input: root = [1,2,3,4,5], subRoot = [2,4,5]

Output: true
Example 2:

Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]

Output: false
Constraints:

0 <= The number of nodes in both trees <= 100.
-100 <= root.val, subRoot.val <= 100
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
	def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

		def check_trees(node1, node2):
			if node1 == None or node2 == None:
				if node1 != node2:
					return False
				return True
			if node1.val != node2.val:
				return False
			return check_trees(node1.left, node2.left) and check_trees(node1.right, node2.right)
		
		def loop_through(node):
			if node is None:
				return False
			if check_trees(node, subRoot):
				return True
			return loop_through(node.left) or loop_through(node.right)
		
		return loop_through(root)