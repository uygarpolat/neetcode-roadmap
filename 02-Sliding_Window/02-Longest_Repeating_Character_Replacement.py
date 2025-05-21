"""
Longest Repeating Character Replacement

https://neetcode.io/problems/longest-repeating-substring-with-replacement

You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2

Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:

Input: s = "AAABABB", k = 1

Output: 5
Constraints:

1 <= s.length <= 1000
0 <= k <= s.length

Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(m) space, where n is the length of the given string and m is the number of unique characters in the string.
"""

from collections import defaultdict

class Solution:
	def characterReplacement(self, s: str, k: int) -> int:

		count = defaultdict(int)
		res = 0
		l = 0
		maxf = 0
		for r in range(len(s)):

			count[s[r]] += 1

			maxf = max(maxf, count[s[r]])

			while (r - l + 1) - maxf > k:
				count[s[l]] -= 1
				l += 1
			res = max(res, r - l + 1)

		return res
    
def main():
	solution = Solution()
	s = "XYYX"
	k = 2
	result = solution.characterReplacement(s, k)
	assert(result == 4)
    
	s = "AAABABB"
	k = 1
	result = solution.characterReplacement(s, k)
	assert(result == 5)

	print("✅ All tests passed!")

if __name__ == "__main__":
    main()

