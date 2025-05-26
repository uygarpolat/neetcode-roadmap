"""
Search a 2D Matrix

https://neetcode.io/problems/search-2d-matrix

You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Example 1:

Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

Output: true
Example 2:

Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15

Output: false
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10000 <= matrix[i][j], target <= 10000

Recommended Time & Space Complexity
You should aim for a solution with O(log(m * n)) time and O(1) space, where m is the number of rows and n is the number of columns in the matrix.
"""
from typing import List

class Solution:
	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

		lo = 0
		n = len(matrix)
		m = len(matrix[0])
		hi = m * n - 1

		while lo <= hi:

			mid = lo + (hi-lo) // 2
			row = mid // m
			col = mid % m
			value = matrix[row][col]

			if value == target:
				return True
			elif value < target:
				lo = mid + 1
			else:
				hi = mid - 1

		return False
	
def main():
	solution = Solution()
	matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
	target = 10
	result = solution.searchMatrix(matrix, target)
	assert(result == True)

	matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
	target = 15
	result = solution.searchMatrix(matrix, target)
	assert(result == False)

	matrix = [[1,1]]
	target = 2
	result = solution.searchMatrix(matrix, target)
	assert(result == False)

	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
