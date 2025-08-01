"""
Rotate Image

https://neetcode.io/problems/rotate-matrix?list=neetcode150

Given a square n x n matrix of integers matrix, rotate it by 90 degrees clockwise.

You must rotate the matrix in-place. Do not allocate another 2D matrix and do the rotation.

Example 1:

Input: matrix = [
  [1,2],
  [3,4]
]

Output: [
  [3,1],
  [4,2]
]
Example 2:

Input: matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

Output: [
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""
from typing import List

class Solution:
	def rotate(self, matrix: List[List[int]]) -> None:
		n = len(matrix)
		for i in range(n):
			for j in range(i+1, n):
				matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

		for row in matrix:
			row.reverse()
        
def main():
	solution = Solution()

	matrix = [[1,2],[3,4]]
	solution.rotate(matrix)
	assert matrix == [[3,1],[4,2]]

	matrix = [[1,2,3],[4,5,6],[7,8,9]]
	solution.rotate(matrix)
	assert matrix == [[7,4,1],[8,5,2],[9,6,3]]

	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
