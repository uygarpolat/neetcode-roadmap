"""
Regular Expression Matching

https://neetcode.io/problems/regular-expression-matching?list=neetcode150

You are given an input string s consisting of lowercase english letters, and a pattern p consisting of lowercase english letters, as well as '.', and '*' characters.

Return true if the pattern matches the entire input string, otherwise return false.

'.' Matches any single character
'*' Matches zero or more of the preceding element.
Example 1:

Input: s = "aa", p = ".b"

Output: false
Explanation: Regardless of which character we choose for the '.' in the pattern, we cannot match the second character in the input string.

Example 2:

Input: s = "nnn", p = "n*"

Output: true
Explanation: '*' means zero or more of the preceding element, 'n'. We choose 'n' to repeat three times.

Example 3:

Input: s = "xyz", p = ".*z"

Output: true
Explanation: The pattern ".*" means zero or more of any character, so we choose ".." to match "xy" and "z" to match "z".

Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
Each appearance of '*', will be preceded by a valid character or '.'.
"""
class Solution:
	def isMatch(self, s: str, p: str) -> bool:

		n = len(s)
		m = len(p)
		memo = {}

		def canExit(index):
			while index < m:
				if index + 1 < m and p[index+1] == '*':
					index += 2
				else:
					return False
			return True

		def dp(index1, index2):
			if index1 == n:
				return canExit(index2)
			if index2 == m:
				return False
			
			if (index1, index2) in memo:
				return memo[(index1, index2)]
			
			answer = False
			if index2 + 1 < m and p[index2+1] == '*':
				if dp(index1, index2+2):
					answer = True
				elif (p[index2] == s[index1] or p[index2] == '.') and dp(index1+1, index2):
					answer = True
			else:
				if p[index2] == s[index1] or p[index2] == '.':
					answer = dp(index1+1, index2+1)
					
			memo[(index1, index2)] = answer
			return answer

		return dp(0, 0)

def main():
	solution = Solution()
	assert solution.isMatch("aa", ".b") == False
	assert solution.isMatch("nnn", "n*") == True
	assert solution.isMatch("xyz", ".*z") == True
	assert solution.isMatch("aa", "a") == False
	assert solution.isMatch("aab", "c*a*b") == True
	assert solution.isMatch("aaa", "aaaa") == False
	assert solution.isMatch("a", "ab*") == True
	assert solution.isMatch("abcd", "d*") == False
	assert solution.isMatch("bbbbba", ".*a*a") == True
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
