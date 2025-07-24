"""
Word Break

https://neetcode.io/problems/word-break?list=neetcode150

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of dictionary words.

You are allowed to reuse words in the dictionary an unlimited number of times. You may assume all dictionary words are unique.

Example 1:

Input: s = "neetcode", wordDict = ["neet","code"]

Output: true
Explanation: Return true because "neetcode" can be split into "neet" and "code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen","ape"]

Output: true
Explanation: Return true because "applepenapple" can be split into "apple", "pen" and "apple". Notice that we can reuse words and also not use all the words.

Example 3:

Input: s = "catsincars", wordDict = ["cats","cat","sin","in","car"]

Output: false
Constraints:

1 <= s.length <= 200
1 <= wordDict.length <= 100
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
"""
from typing import List

class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> bool:

		n = len(s)
		memo = [None] * (n+1)

		def dp(index):
			if index == n:
				return True
			
			if memo[index] is not None:
				return memo[index]

			for word in wordDict:
				end = index + len(word)
				if end <= n and s[index:end] == word:
					if dp(end):
						memo[index] = True
						return True
			memo[index] = False

			return False

		return dp(0)
    
def main():
	solution = Solution()
	assert solution.wordBreak("neetcode", ["neet","code"]) == True
	assert solution.wordBreak("applepenapple", ["apple","pen","ape"]) == True
	assert solution.wordBreak("catsincars", ["cats","cat","sin","in","car"]) == False
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
