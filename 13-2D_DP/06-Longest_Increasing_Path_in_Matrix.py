"""
Longest Increasing Path in Matrix

https://neetcode.io/problems/longest-increasing-path-in-matrix?list=neetcode150

You are given a 2-D grid of integers matrix, where each integer is greater than or equal to 0.

Return the length of the longest strictly increasing path within matrix.

From each cell within the path, you can move either horizontally or vertically. You may not move diagonally.

Example 1:

Input: matrix = [[5,5,3],[2,3,6],[1,1,1]]

Output: 4
Explanation: The longest increasing path is [1, 2, 3, 6] or [1, 2, 3, 5].

Example 2:

Input: matrix = [[1,2,3],[2,1,4],[7,6,5]]

Output: 7
Explanation: The longest increasing path is [1, 2, 3, 4, 5, 6, 7].

Constraints:

1 <= matrix.length, matrix[i].length <= 100
"""
from typing import List

class Solution:
	def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

		rowCount = len(matrix)
		colCount = len(matrix[0])
		memo = {}

		def dp(x,y,num,flag):
			if not 0 <= x < rowCount or not 0 <= y < colCount:
				return 0
			
			if matrix[x][y] <= num and flag:
				return 0
			
			num = matrix[x][y]
		
			if (x,y) in memo:
				return memo[(x,y)]
			
			memo[(x,y)] = 1 + max(dp(x+1,y,num,True),dp(x,y+1,num,True),dp(x-1,y,num,True),dp(x,y-1,num,True))
			return memo[(x,y)]

		for i in range(rowCount * colCount):
			x = i // colCount
			y = i % colCount
			if (x,y) not in memo:
				memo[(x,y)] = dp(x,y,matrix[x][y],False)

		return max(memo.values())

def main():
	solution = Solution()
	assert solution.longestIncreasingPath([[5,5,3],[2,3,6],[1,1,1]]) == 4
	assert solution.longestIncreasingPath([[1,2,3],[2,1,4],[7,6,5]]) == 7
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
