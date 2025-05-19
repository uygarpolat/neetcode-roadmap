"""
Valid Sudoku
 
You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.

Example 1:

Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: true
Example 2:

Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: false
Explanation: There are two 1's in the top-left 3x3 sub-box.

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.

Recommended Time & Space Complexity
You should aim for a solution as good or better than O(n^2) time and O(n^2) space, where n is the number of rows in the square grid.
"""
from typing import List
from collections import defaultdict

class Solution:
	def isValidSudoku(self, board: List[List[str]]) -> bool:

		horizontals = defaultdict(list)
		verticals = defaultdict(list)
		squares = defaultdict(list)

		for i, row in enumerate(board):
			for j, cell in enumerate(row):

				if cell == '.':
					continue

				cell_int = int(cell)

				horizontals[i].append(cell_int)
				verticals[j].append(cell_int)
				squares[(i//3,j//3)].append(cell_int)

		for horizontal in horizontals:
			if len(horizontals[horizontal]) != len(set(horizontals[horizontal])):
				return False
		for vertical in verticals:
			if len(verticals[vertical]) != len(set(verticals[vertical])):
				return False
		for square in squares:
			if len(squares[square]) != len(set(squares[square])):
				return False

		return True
    
def main():
	solution = Solution()
	board = \
	[["1","2",".",".","3",".",".",".","."],
	["4",".",".","5",".",".",".",".","."],
	[".","9","8",".",".",".",".",".","3"],
	["5",".",".",".","6",".",".",".","4"],
	[".",".",".","8",".","3",".",".","5"],
	["7",".",".",".","2",".",".",".","6"],
	[".",".",".",".",".",".","2",".","."],
	[".",".",".","4","1","9",".",".","8"],
	[".",".",".",".","8",".",".","7","9"]]
	result = solution.isValidSudoku(board)
	assert(result == True)
    
	board = \
	[["1","2",".",".","3",".",".",".","."],
	["4",".",".","5",".",".",".",".","."],
	[".","9","1",".",".",".",".",".","3"],
	["5",".",".",".","6",".",".",".","4"],
	[".",".",".","8",".","3",".",".","5"],
	["7",".",".",".","2",".",".",".","6"],
	[".",".",".",".",".",".","2",".","."],
	[".",".",".","4","1","9",".",".","8"],
	[".",".",".",".","8",".",".","7","9"]]
	result = solution.isValidSudoku(board)
	assert(result == False)

	print("✅ All tests passed!")

if __name__ == "__main__":
    main()
