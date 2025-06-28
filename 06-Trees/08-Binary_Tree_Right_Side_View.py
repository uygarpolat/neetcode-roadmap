"""
Binary Tree Right Side View

https://neetcode.io/problems/binary-tree-right-side-view?list=neetcode150

You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.

Example 1:

Input: root = [1,2,3]

Output: [1,3]
Example 2:

Input: root = [1,2,3,4,5,6,7]

Output: [1,3,7]
Constraints:

0 <= number of nodes in the tree <= 100
-100 <= Node.val <= 100
"""
from typing import List, Optional
from collections import deque

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

		if not root:
			return []
		
		queue = deque([root])
		result = []

		while queue:
			rightmost_node = None
			len_q = len(queue)

			for _ in range(len_q):
				node = queue.popleft()
				if node:
					rightmost_node = node
					queue.append(node.left)
					queue.append(node.right)
			if rightmost_node:
				result.append(rightmost_node.val)
				
		return result
