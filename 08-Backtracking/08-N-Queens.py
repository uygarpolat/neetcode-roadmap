"""
N-Queens

https://neetcode.io/problems/n-queens?list=neetcode150

The n-queens puzzle is the problem of placing n queens on an n x n chessboard so that no two queens can attack each other.

A queen in a chessboard can attack horizontally, vertically, and diagonally.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a unique board layout where the queen pieces are placed. 'Q' indicates a queen and '.' indicates an empty space.

You may return the answer in any order.

Example 1:

Input: n = 4

Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There are two different solutions to the 4-queens puzzle.

Example 2:

Input: n = 1

Output: [["Q"]]
Constraints:

1 <= n <= 8
"""
from typing import List

class Solution:
	def solveNQueens(self, n: int) -> List[List[str]]:
		
		fullList = []
		board = [["."] * n for i in range(n)]

		def canPlace(row, col):
			for i, rows in enumerate(board):
				for j, cell in enumerate(rows):
					if board[i][j] == "Q":
						if i == row or j == col or abs(i-row) == abs(j-col):
							return False
			return True

		def backtrack(row):
			if row == n:
				fullList.append([''.join(row) for row in board])
				return
			
			for col in range(n):
				if canPlace(row, col):
					board[row][col] = "Q"
					backtrack(row+1)
					board[row][col] = "."

		backtrack(0)
		return fullList
    
def main():
	solution = Solution()
	result = solution.solveNQueens(4)
	assert result == [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
	assert solution.solveNQueens(1) == [["Q"]]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
