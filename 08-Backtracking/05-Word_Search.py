"""
Word Search

https://neetcode.io/problems/search-for-word?list=neetcode150

Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.

For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

Example 1:

Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "CAT"

Output: true
Example 2:

Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "BAT"

Output: false
Constraints:

1 <= board.length, board[i].length <= 5
1 <= word.length <= 10
board and word consists of only lowercase and uppercase English letters.
"""
from typing import List

class Solution:
	def exist(self, board: List[List[str]], word: str) -> bool:
		
		row_count = len(board)
		col_count = len(board[0])
		visiting = set()
		directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        
		def dfs(row, col, index, visited):
			if index == len(word):
				return True
            
			if not (0 <= row < row_count) \
				or not (0 <= col < col_count) \
				or (row, col) in visited \
				or board[row][col] != word[index]:
				return False
            
			visited.add((row, col))
            
			for dr, dc in directions:
				if dfs(row + dr, col + dc, index + 1, visited):
					return True
            
			visited.remove((row, col))

			return False
        	
		for row in range(row_count):
			for col in range(col_count):
				if dfs(row, col, 0, visiting):
					return True
        
		return False
	
def main():
	solution = Solution()
	assert solution.exist([["A","B","C","D"],["S","A","A","T"],["A","C","A","E"]], "CAT") == True
	assert solution.exist([["A","B","C","D"],["S","A","A","T"],["A","C","A","E"]], "BAT") == False
	print("✅ All tests passed!")
	
if __name__ == "__main__":
	main()
