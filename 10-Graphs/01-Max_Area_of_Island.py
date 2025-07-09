"""
Max Area of Island

https://neetcode.io/problems/max-area-of-island?list=neetcode150

You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).

An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

The area of an island is defined as the number of cells within the island.

Return the maximum area of an island in grid. If no island exists, return 0.

Example 1:

Input: grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

Output: 6
Explanation: 1's cannot be connected diagonally, so the maximum area of the island is 6.

Constraints:

1 <= grid.length, grid[i].length <= 50
"""
from typing import List

class Solution:
	def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
		dirs = [[0,1], [1,0], [-1,0], [0,-1]]
		result = 0

		def floodfill(i, j):
			if grid[i][j] == 0:
				return 0
			grid[i][j] = 0
			res = 1
			for first, second in dirs:
				new_i = i + first
				new_j = j + second
				if not 0 <= new_i < len(grid) \
					or not 0 <= new_j < len(grid[0]) \
					or grid[new_i][new_j] == 0:
					continue
				
				res += floodfill(new_i, new_j)
			return res

		for i, rows in enumerate(grid):
			for j in range(len(rows)):
				ff = floodfill(i, j)
				result = max(result, ff)

		return result

def main():
	solution = Solution()
	assert solution.maxAreaOfIsland([[0,1,1,0,1],[1,0,1,0,1],[0,1,1,0,1],[0,1,0,0,1]]) == 6
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
