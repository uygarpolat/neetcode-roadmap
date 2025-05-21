"""
Permutation in String

https://neetcode.io/problems/permutation-string

You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

Example 1:

Input: s1 = "abc", s2 = "lecabee"

Output: true
Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

Example 2:

Input: s1 = "abc", s2 = "lecaabee"

Output: false
Constraints:

1 <= s1.length, s2.length <= 1000
"""
class Solution:
	def checkInclusion(self, s1: str, s2: str) -> bool:

		if len(s1) > len(s2):
			return False
		
		count_s1 = [0] * 26
		count_temp = [0] * 26
		base = ord("a")
		offset = len(s1) - 1

		for ch in s1:
			count_s1[ord(ch) - base] += 1
		for i in range(len(s1)):
			count_temp[ord(s2[i]) - base] += 1

		if count_s1 == count_temp:
			return True

		for i in range(1, len(s2) - offset):
			count_temp[ord(s2[i-1]) - base] -= 1
			count_temp[ord(s2[i+offset]) - base] += 1
			if count_s1 == count_temp:
				return True

		return False

def main():
	solution = Solution()
	s1 = "abc"
	s2 = "lecabee"
	result = solution.checkInclusion(s1, s2)
	assert(result == True)
    
	s1 = "abc"
	s2 = "lecaabee"
	result = solution.checkInclusion(s1, s2)
	assert(result == False)
    
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
