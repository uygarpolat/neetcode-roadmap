"""
Word Search II

https://neetcode.io/problems/search-for-word-ii?list=neetcode150

Given a 2-D grid of characters board and a list of strings words, return all words that are present in the grid.

For a word to be present it must be possible to form the word with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

Example 1:

Input:
board = [
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
],
words = ["bat","cat","back","backend","stack"]

Output: ["cat","back","backend"]
Example 2:

Input:
board = [
  ["x","o"],
  ["x","o"]
],
words = ["xoxo"]

Output: []
Constraints:

1 <= board.length, board[i].length <= 12
board[i] consists only of lowercase English letter.
1 <= words.length <= 30,000
1 <= words[i].length <= 10
words[i] consists only of lowercase English letters.
All strings within words are distinct.
"""
from typing import List

class MyTrie:
	def __init__(self):
		self.children = {}
		self.endOfWord = False
		self.index = -1

class Solution:
	def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
		
		dirs = [[0,1], [1,0], [-1,0], [0,-1]]
		row_length = len(board[0])
		col_length = len(board)
		trie = MyTrie()
		result = []

		def add(word, index):
			current = trie
			for c in word:
				if c not in current.children:
					current.children[c] = MyTrie()
				current = current.children[c]
			current.endOfWord = True
			current.index = index

		def search(localTrie: MyTrie, row: int, col: int, visited: set):
			if localTrie.endOfWord:
				result.append(words[localTrie.index])
				localTrie.index = -1
				localTrie.endOfWord = False

			visited.add((row, col))

			for dir in dirs:
				newRow = row + dir[0]
				newCol = col + dir[1]
				if not 0 <= newRow < col_length or not 0 <= newCol < row_length:
					continue
				if (newRow, newCol) in visited:
					continue
				if board[newRow][newCol] in localTrie.children:
					search(localTrie.children[board[newRow][newCol]], newRow, newCol, visited)

			visited.remove((row,col))

		for index, word in enumerate(words):
			add(word, index)

		for cell in range(row_length * col_length):
			row = cell // row_length
			col = cell % row_length
			c = board[row][col]
			if c in trie.children:
				search(trie.children[c], row, col, set())

		return result
	
def main():
	solution = Solution()
	assert solution.findWords([["a","b","c","d"],["s","a","a","t"],["a","c","k","e"],["a","c","d","n"]], ["bat","cat","back","backend","stack"]) == ['back', 'backend', 'cat']
	assert solution.findWords([["x","o"],["x","o"]], ["xoxo"]) == []
	assert solution.findWords([["a"]],["a"]) == ["a"]
	assert solution.findWords([["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]], ["oa","oaa"]) == ["oa","oaa"]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
