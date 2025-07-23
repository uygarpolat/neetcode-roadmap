"""
Palindromic Substrings

https://neetcode.io/problems/palindromic-substrings?list=neetcode150

Given a string s, return the number of substrings within s that are palindromes.

A palindrome is a string that reads the same forward and backward.

Example 1:

Input: s = "abc"

Output: 3
Explanation: "a", "b", "c".

Example 2:

Input: s = "aaa"

Output: 6
Explanation: "a", "a", "a", "aa", "aa", "aaa". Note that different substrings are counted as different palindromes even if the string contents are the same.

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
"""
class Solution:
	def countSubstrings(self, s: str) -> int:

		n = len(s)
		count = 0

		for i in range(n):
			l, r = i, i
			while l >= 0 and r < n and s[l] == s[r]:
				count += 1
				l -= 1
				r += 1
			l, r = i, i+1
			while l >= 0 and r < n and s[l] == s[r]:
				count += 1
				l -= 1
				r += 1

		return count

def main():
	solution = Solution()
	assert solution.countSubstrings("abc") == 3
	assert solution.countSubstrings("aaa") == 6
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
