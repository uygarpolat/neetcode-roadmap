"""
Binary Tree Level Order Traversal

https://neetcode.io/problems/level-order-traversal-of-binary-tree?list=neetcode150

Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

Example 1:

Input: root = [1,2,3,4,5,6,7]

Output: [[1],[2,3],[4,5,6,7]]
Example 2:

Input: root = [1]

Output: [[1]]
Example 3:

Input: root = []

Output: []
Constraints:

0 <= The number of nodes in both trees <= 1000.
-1000 <= Node.val <= 1000
"""
from typing import Optional, List
from collections import deque

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
		if not root:
			return []
        
		queue = deque([root])
		result = []

		while queue:
			level_len = len(queue)
			level_result = []

			for _ in range(level_len):
				node = queue.popleft()
				level_result.append(node.val)
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)

			result.append(level_result)

		return result
