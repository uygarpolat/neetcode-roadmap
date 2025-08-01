"""
Spiral Matrix

https://neetcode.io/problems/spiral-matrix?list=neetcode150

Given an m x n matrix of integers matrix, return a list of all elements within the matrix in spiral order.

Example 1:

Input: matrix = [[1,2],[3,4]]

Output: [1,2,4,3]
Example 2:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]

Output: [1,2,3,6,9,8,7,4,5]
Example 3:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

Output: [1,2,3,4,8,12,11,10,9,5,6,7]
Constraints:

1 <= matrix.length, matrix[i].length <= 10
-100 <= matrix[i][j] <= 100
"""
from typing import List

class Solution:
	def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
		result = []
		rowIter = len(matrix) - 1
		colIter = len(matrix[0])
		directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
		steps = [colIter, rowIter]
		r, c, d = 0, -1, 0

		while steps[d % 2]:
			for i in range(steps[d % 2]):
				r += directions[d][0]
				c += directions[d][1]
				result.append(matrix[r][c])
			steps[d % 2] -= 1
			d += 1
			d %= 4

		return result

def main():
	solution = Solution()
	assert solution.spiralOrder([[1,2],[3,4]]) == [1,2,4,3]
	assert solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
	assert solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
