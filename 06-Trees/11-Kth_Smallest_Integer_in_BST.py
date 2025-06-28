"""
Kth Smallest Integer in BST

https://neetcode.io/problems/kth-smallest-integer-in-bst?list=neetcode150

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.
Example 1:

Input: root = [2,1,3], k = 1

Output: 1
Example 2:

Input: root = [4,3,5,2,null], k = 4

Output: 5
Constraints:

1 <= k <= The number of nodes in the tree <= 1000.
0 <= Node.val <= 1000
"""
from typing import Optional

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
		result = 0
		def dfs(node: TreeNode, count: int) -> int:
			nonlocal result
			if not node or result:
				return count
			count = dfs(node.left, count)
			if result:
				return count
			count += 1
			if count == k:
				result = node.val
				return count
			return dfs(node.right, count)
		dfs(root, 0)
		return result
	
def main():
	solution = Solution()

	root = TreeNode(4, TreeNode(3, TreeNode(2), None), TreeNode(5))
	assert solution.kthSmallest(root, 4) == 5

	root = TreeNode(2, TreeNode(1), TreeNode(3))
	assert solution.kthSmallest(root, 1) == 1
	assert solution.kthSmallest(root, 2) == 2

	root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1), None), TreeNode(4)), TreeNode(6))
	assert solution.kthSmallest(root, 1) == 1 or print(solution.kthSmallest(root, 1)) or False
	assert solution.kthSmallest(root, 2) == 2 or print(solution.kthSmallest(root, 2)) or False
	assert solution.kthSmallest(root, 3) == 3 or print(solution.kthSmallest(root, 3)) or False
	assert solution.kthSmallest(root, 4) == 4 or print(solution.kthSmallest(root, 4)) or False
	assert solution.kthSmallest(root, 5) == 5 or print(solution.kthSmallest(root, 5)) or False
	assert solution.kthSmallest(root, 6) == 6 or print(solution.kthSmallest(root, 6)) or False
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
        