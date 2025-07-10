"""
Islands and Treasure

https://neetcode.io/problems/islands-and-treasure?list=neetcode150

You are given a m x n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.

Example 1:

Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]
Example 2:

Input: [
  [0,-1],
  [2147483647,2147483647]
]

Output: [
  [0,-1],
  [1,2]
]
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is one of {-1, 0, 2147483647}
"""
from typing import List
from collections import deque

class Solution:
	def islandsAndTreasure(self, grid: List[List[int]]) -> None:

		dirs = [[1,0],[0,1],[-1,0],[0,-1]]
		q = deque()

		for i, rows in enumerate(grid):
			for j, _ in enumerate(rows):
				if grid[i][j] == 0:
					q.append((i,j,0))

		while q:
			i, j, distance = q.popleft()
			for dir in dirs:
				new_i, new_j = i + dir[0], j + dir[1]
				if not 0 <= new_i < len(grid) or not 0 <= new_j < len(grid[0]):
					continue
				if grid[new_i][new_j] != 2**31 - 1:
					continue
				grid[new_i][new_j] = distance + 1
				q.append((new_i, new_j, distance + 1))

	
def main():
	solution = Solution()
	input = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
	solution.islandsAndTreasure(input)
	assert input == [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

	input = [[0,-1],[2147483647,2147483647]]
	solution.islandsAndTreasure(input)
	assert input == [[0,-1],[1,2]]

	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
