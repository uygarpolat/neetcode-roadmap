"""
Palindrome Partitioning

https://neetcode.io/problems/palindrome-partitioning?list=neetcode150

Given a string s, split s into substrings where every substring is a palindrome. Return all possible lists of palindromic substrings.

You may return the solution in any order.

Example 1:

Input: s = "aab"

Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"

Output: [["a"]]
Constraints:

1 <= s.length <= 20
s contains only lowercase English letters.
"""
from typing import List

class Solution:
	def partition(self, s: str) -> List[List[str]]:

		def isPalindrome(word):
			l = 0
			r = len(word) - 1
			while l < r:
				if word[l] != word[r]:
					return False
				l, r = l+1, r-1
			return True

		result = []
		substrings = []

		def dfs(index):
			if index == len(s):
				result.append(substrings.copy())
				return
			
			for i in range(index, len(s)):
				if isPalindrome(s[index: i+1]):
					substrings.append(s[index: i+1])
					dfs(i+1)
					substrings.pop()

		dfs(0)
		return result
	
def main():
	solution = Solution()
	assert solution.partition("aab") == [["a","a","b"],["aa","b"]]
	assert solution.partition("a") == [["a"]]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
