"""
Rotting Fruit

https://neetcode.io/problems/rotting-fruit?list=neetcode150

You are given a 2-D matrix grid. Each cell can have one of three possible values:

0 representing an empty cell
1 representing a fresh fruit
2 representing a rotten fruit
Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.

Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.

Example 1:

Input: grid = [[1,1,0],[0,1,1],[0,1,2]]

Output: 4
Example 2:

Input: grid = [[1,0,1],[0,2,0],[1,0,1]]

Output: -1
Constraints:

1 <= grid.length, grid[i].length <= 10
"""
from typing import List
from collections import deque

class Solution:
	def orangesRotting(self, grid: List[List[int]]) -> int:

		dirs = [[1,0],[0,1],[-1,0],[0,-1]]
		q = deque()
		time = 0

		for i, rows in enumerate(grid):
			for j, _ in enumerate(rows):
				if grid[i][j] == 2:
					q.append((i,j,time))

		while q:
			i, j, time = q.popleft()

			for dir in dirs:
				new_i = i + dir[0]
				new_j = j + dir[1]
				if not 0 <= new_i < len(grid) or not 0 <= new_j < len(grid[0]):
					continue
				if grid[new_i][new_j] != 1:
					continue
				grid[new_i][new_j] = 2
				q.append((new_i, new_j, time + 1))

		for i, rows in enumerate(grid):
			for j, _ in enumerate(rows):
				if grid[i][j] == 1:
					return -1

		return time
    
def main():
	solution = Solution()
	assert solution.orangesRotting([[1,1,0],[0,1,1],[0,1,2]]) == 4
	assert solution.orangesRotting([[1,0,1],[0,2,0],[1,0,1]]) == -1
	assert solution.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
