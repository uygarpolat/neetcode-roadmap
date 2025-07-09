"""
Number of Islands

https://neetcode.io/problems/count-number-of-islands?list=neetcode150

Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).

Example 1:

Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
Output: 1
Example 2:

Input: grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
Output: 4
Constraints:

1 <= grid.length, grid[i].length <= 100
grid[i][j] is '0' or '1'.
"""
from typing import List

class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		dirs = [[0,1], [1,0], [-1,0], [0,-1]]
		visited = set()
		result = 0

		def floodfill(i, j):
			for first, second in dirs:
				new_i = i + first
				new_j = j + second
				if not 0 <= new_i < len(grid) \
					or not 0 <= new_j < len(grid[0]) \
					or grid[new_i][new_j] == "0" \
					or (new_i, new_j) in visited:
					continue
				visited.add((new_i,new_j))
				floodfill(new_i, new_j)

		for i, rows in enumerate(grid):
			for j in range(len(rows)):
				if grid[i][j] == "1" and (i,j) not in visited:
					result += 1
					visited.add((i,j))
					floodfill(i, j)

		return result
	
def main():
	solution = Solution()
	assert solution.numIslands([["0","1","1","1","0"],["0","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]) == 1
	assert solution.numIslands([["1","1","0","0","1"],["1","1","0","0","1"],["0","0","1","0","0"],["0","0","0","1","1"]]) == 4
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
