"""
Longest Palindromic Substring

https://neetcode.io/problems/longest-palindromic-substring?list=neetcode150

Given a string s, return the longest substring of s that is a palindrome.

A palindrome is a string that reads the same forward and backward.

If there are multiple palindromic substrings that have the same length, return any one of them.

Example 1:

Input: s = "ababd"

Output: "bab"
Explanation: Both "aba" and "bab" are valid answers.

Example 2:

Input: s = "abbc"

Output: "bb"
Constraints:

1 <= s.length <= 1000
s contains only digits and English letters.
"""
class Solution:
	def longestPalindrome(self, s: str) -> str:
		n = len(s)
		resLen = 0
		resId = 0

		for i in range(n):
			l, r = i, i
			while l >= 0 and r < n and s[l] == s[r]:
				if r - l + 1 > resLen:
					resId = l
					resLen = r - l + 1
				l -= 1
				r += 1

			l, r = i, i+1
			while l >= 0 and r < n and s[l] == s[r]:
				if r - l + 1 > resLen:
					resId = l
					resLen = r - l + 1
				l -= 1
				r += 1

		return s[resId:resId+resLen]

def main():
	solution = Solution()
	assert solution.longestPalindrome("ababd") == "aba"
	assert solution.longestPalindrome("abbc") == "bb"
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
