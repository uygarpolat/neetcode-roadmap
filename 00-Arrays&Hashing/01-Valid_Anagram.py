"""
Valid Anagram

Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.
"""
from collections import Counter

class Solution:
	def isAnagram(self, s: str, t: str) -> bool:

		# Solution 1: time: O(n logn), space: O(n)
		# return ''.join(sorted(s)) == ''.join(sorted(t))

		# Solution 2: time: O(n+m), space: O(1)
		if len(s) != len(t):
			return False
		count = [0] * 26
		base = ord('a')
		for c in s:
			count[ord(c)-base] += 1
		for c in t:
			count[ord(c)-base] -= 1
			if count[ord(c)-base] < 0:
				return False
		return True

def main():
	solution = Solution()
	s = "racecar"
	t = "carrace"
	result = solution.isAnagram(s, t)
	print(result) # Expected outcome: True
    
	s = "jar"
	t = "jam"
	result = solution.isAnagram(s, t)
	print(result) # Expected outcome: False
    
if __name__ == "__main__":
    main()
