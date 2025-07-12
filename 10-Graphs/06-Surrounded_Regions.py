"""
Surrounded Regions

https://neetcode.io/problems/surrounded-regions?list=neetcode150

You are given a 2-D matrix board containing 'X' and 'O' characters.

If a continous, four-directionally connected group of 'O's is surrounded by 'X's, it is considered to be surrounded.

Change all surrounded regions of 'O's to 'X's and do so in-place by modifying the input board.

Example 1:

Input: board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","O","O","X"],
  ["X","X","X","O"]
]

Output: [
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","O"]
]
Explanation: Note that regions that are on the border are not considered surrounded regions.

Constraints:

1 <= board.length, board[i].length <= 200
board[i][j] is 'X' or 'O'.
"""
from typing import List

class Solution:
	def solve(self, board: List[List[str]]) -> None:

		dirs = [[1,0],[0,1],[-1,0],[0,-1]]
		rowCount, colCount = len(board), len(board[0])
		visited = set()

		def dfs(i,j, region: List[tuple]):
			if not 0 <= i < rowCount or not 0 <= j < colCount:
				return False
			if board[i][j] == "X" or (i,j) in visited:
				return True

			visited.add((i,j))
			region.append((i,j))
			isSurrounded = True
			for dir in dirs:
				if not dfs(i+dir[0],j+dir[1], region):
					isSurrounded = False
			return isSurrounded
			
		for i in range(rowCount):
			for j in range(colCount):
				if board[i][j] == "O" and (i,j) not in visited:
					region = []
					if dfs(i, j, region):
						for x, y in region:
							board[x][y] = "X"
	
def main():
	solution = Solution()
	input = [["X","X","X","X"],["X","O","O","X"],["X","O","O","X"],["X","X","X","O"]]
	solution.solve(input)
	assert input == [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","X","X","O"]]

	input = [["X","X","X","X"],["X","O","O","X"],["X","O","O","X"],["X","O","X","O"]]
	solution.solve(input)
	assert input == [["X","X","X","X"],["X","O","O","X"],["X","O","O","X"],["X","O","X","O"]]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
