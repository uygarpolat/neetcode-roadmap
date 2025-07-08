"""
Design Add and Search Word Data Structure

https://neetcode.io/problems/design-word-search-data-structure?list=neetcode150

Design a data structure that supports adding new words and searching for existing words.

Implement the WordDictionary class:

void addWord(word) Adds word to the data structure.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
Example 1:

Input:
["WordDictionary", "addWord", "day", "addWord", "bay", "addWord", "may", "search", "say", "search", "day", "search", ".ay", "search", "b.."]

Output:
[null, null, null, null, false, true, true, true]

Explanation:
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("day");
wordDictionary.addWord("bay");
wordDictionary.addWord("may");
wordDictionary.search("say"); // return false
wordDictionary.search("day"); // return true
wordDictionary.search(".ay"); // return true
wordDictionary.search("b.."); // return true
Constraints:

1 <= word.length <= 20
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 10,000 calls will be made to addWord and search.
"""
class MyTree:
	def __init__(self):
		self.children = {}
		self.endOfWord = False

class WordDictionary:

	def __init__(self):
		self.root = MyTree()

	def addWord(self, word: str) -> None:
		current = self.root
		for c in word:
			if c not in current.children:
				current.children[c] = MyTree()
			current = current.children[c]
		current.endOfWord = True
          
	def search(self, word: str) -> bool:
		current = self.root
		for i, c in enumerate(word):
			if c == '.':
				for c2 in current.children:
					if self.search(word[:i] + c2 + word[i+1:]):
						return True
				return False
			if c not in current.children:
				return False
			current = current.children[c]
		return current.endOfWord

def main():
	wordDictionary = WordDictionary()
	wordDictionary.addWord("day")
	wordDictionary.addWord("bay")
	wordDictionary.addWord("may")
	assert wordDictionary.search("say") == False
	assert wordDictionary.search("day") == True
	assert wordDictionary.search(".ay") == True
	assert wordDictionary.search("b..") == True
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
