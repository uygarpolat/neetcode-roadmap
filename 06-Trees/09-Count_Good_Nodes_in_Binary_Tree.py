"""
Count Good Nodes in Binary Tree

https://neetcode.io/problems/count-good-nodes-in-binary-tree?list=neetcode150

Within a binary tree, a node x is considered good if the path from the root of the tree to the node x contains no nodes with a value greater than the value of node x

Given the root of a binary tree root, return the number of good nodes within the tree.

Example 1:

Input: root = [2,1,1,3,null,1,5]

Output: 3

Example 2:

Input: root = [1,2,-1,3,4]

Output: 4
Constraints:

1 <= number of nodes in the tree <= 100
-100 <= Node.val <= 100
"""
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def goodNodes(self, root: TreeNode) -> int:
		if not root:
			return 0
		counter = 0
		def traverseNodes(node: TreeNode, priorMax: int):
			nonlocal counter
			if not node:
				return
			if node.val >= priorMax:
				counter += 1
				priorMax = node.val
			traverseNodes(node.left, priorMax)
			traverseNodes(node.right, priorMax)
		traverseNodes(root, root.val)
		return counter
	
def main():
	solution = Solution()
	
	root = TreeNode(2, TreeNode(1, TreeNode(3), None), TreeNode(1, TreeNode(1), TreeNode(5)))
	assert solution.goodNodes(root) == 3
	
	root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(-1))
	assert solution.goodNodes(root) == 4

	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
