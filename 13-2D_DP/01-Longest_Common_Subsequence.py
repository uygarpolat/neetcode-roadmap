"""
Longest Common Subsequence

https://neetcode.io/problems/longest-common-subsequence?list=neetcode150

Given two strings text1 and text2, return the length of the longest common subsequence between the two strings if one exists, otherwise return 0.

A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

For example, "cat" is a subsequence of "crabt".
A common subsequence of two strings is a subsequence that exists in both strings.

Example 1:

Input: text1 = "cat", text2 = "crabt" 

Output: 3 
Explanation: The longest common subsequence is "cat" which has a length of 3.

Example 2:

Input: text1 = "abcd", text2 = "abcd"

Output: 4
Example 3:

Input: text1 = "abcd", text2 = "efgh"

Output: 0
Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""
class Solution:
	def longestCommonSubsequence(self, text1: str, text2: str) -> int:

		len1 = len(text1)
		len2 = len(text2)
		memo = [[0] * len2 for _ in range(len1)]

		def dp(i, j):
			if i >= len1 or j >= len2:
				return 0
			if memo[i][j]:
				return memo[i][j]
			if text1[i] == text2[j]:
				memo[i][j] = 1 + dp(i+1, j+1)
			else:
				memo[i][j] = max(dp(i,j+1), dp(i+1,j))
			return memo[i][j]
		return dp(0,0)

def main():
	solution = Solution()
	assert solution.longestCommonSubsequence("cat", "crabt") == 3
	assert solution.longestCommonSubsequence("abcd", "abcd") == 4
	assert solution.longestCommonSubsequence("abcd", "efgh") == 0
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
