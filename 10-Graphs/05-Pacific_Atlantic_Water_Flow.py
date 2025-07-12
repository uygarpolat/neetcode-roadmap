"""
Pacific Atlantic Water Flow

https://neetcode.io/problems/pacific-atlantic-water-flow?list=neetcode150

You are given a rectangular island heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The islands borders the Pacific Ocean from the top and left sides, and borders the Atlantic Ocean from the bottom and right sides.

Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell with height equal or lower. Water can also flow into the ocean from cells adjacent to the ocean.

Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans. Return it as a 2D list where each element is a list [r, c] representing the row and column of the cell. You may return the answer in any order.

Example 1:

Input: heights = [
  [4,2,7,3,4],
  [7,4,6,4,7],
  [6,3,5,3,6]
]

Output: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]
Example 2:

Input: heights = [[1],[1]]

Output: [[0,0],[0,1]]
Constraints:

1 <= heights.length, heights[r].length <= 100
0 <= heights[r][c] <= 1000
"""
from typing import List

class Solution:
	def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
		rowCount = len(heights)
		colCount = len(heights[0])
		pacific = set()
		atlantic = set()

		def dfs(r, c, visited, prevHeight):
			if ((r, c) in visited or 
				not 0 <= r < rowCount or
				not 0 <= c < colCount or
				heights[r][c] < prevHeight
			):
				return
			visited.add((r, c))
			dfs(r + 1, c, visited, heights[r][c])
			dfs(r - 1, c, visited, heights[r][c])
			dfs(r, c + 1, visited, heights[r][c])
			dfs(r, c - 1, visited, heights[r][c])
	
		for i in range(rowCount):
			for j in range(colCount):
				if i == 0 or j == 0:
					dfs(i,j, pacific, heights[i][j])
				if i == rowCount-1 or j == colCount-1:
					dfs(i,j, atlantic, heights[i][j])

		result = []
		for r in range(rowCount):
			for c in range(colCount):
				if (r, c) in pacific and (r, c) in atlantic:
					result.append([r, c])

		return result
    
def main():
	solution = Solution()
	assert solution.pacificAtlantic([[4,2,7,3,4],[7,4,6,4,7],[6,3,5,3,6]]) == [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]
	assert solution.pacificAtlantic([[1],[1]]) == [[0,0],[1,0]]
	print("✅ All tests passed!")

if __name__ == "__main__":
    main()
