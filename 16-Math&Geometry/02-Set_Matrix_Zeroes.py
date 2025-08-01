"""
Set Matrix Zeroes

https://neetcode.io/problems/set-zeroes-in-matrix?list=neetcode150

Given an m x n matrix of integers matrix, if an element is 0, set its entire row and column to 0's.

You must update the matrix in-place.

Follow up: Could you solve it using O(1) space?

Example 1:

Input: matrix = [
  [0,1],
  [1,0]
]

Output: [
  [0,0],
  [0,0]
]
Example 2:

Input: matrix = [
  [1,2,3],
  [4,0,5],
  [6,7,8]
]

Output: [
  [1,0,3],
  [0,0,0],
  [6,0,8]
]
Constraints:

1 <= matrix.length, matrix[0].length <= 100
-2^31 <= matrix[i][j] <= (2^31) - 1
"""
from typing import List

class Solution:
	def setZeroes(self, matrix: List[List[int]]) -> None:
		rowCount = len(matrix)
		colCount = len(matrix[0])

		first_row_zero = any(matrix[0][j] == 0 for j in range(colCount))
		first_col_zero = any(matrix[i][0] == 0 for i in range(rowCount))

		for i in range(1, rowCount):
			for j in range(1, colCount):
				if matrix[i][j] == 0:
					matrix[0][j] = 0
					matrix[i][0] = 0
		
		for i in range(1, rowCount):
			for j in range(1, colCount):
				if matrix[0][j] == 0 or matrix[i][0] == 0:
					matrix[i][j] = 0

		if first_row_zero:
			matrix[0] = [0] * colCount

		if first_col_zero:
			for row in matrix:
				row[0] = 0

def main():
	solution = Solution()

	matrix = [[0,1],[1,0]]
	solution.setZeroes(matrix)
	assert matrix == [[0,0],[0,0]]

	matrix = [[1,2,3],[4,0,5],[6,7,8]]
	solution.setZeroes(matrix)
	assert matrix == [[1,0,3],[0,0,0],[6,0,8]]

	matrix = [[1,2,3],[4,0,0],[6,7,8]]
	solution.setZeroes(matrix)
	assert matrix == [[1,0,0],[0,0,0],[6,0,0]]

	matrix = [[0,1],[1,1]]
	solution.setZeroes(matrix)
	assert matrix == [[0,0],[0,1]]

	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
