"""
Minimum Window Substring

https://neetcode.io/problems/minimum-window-with-characters

Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.

Example 1:

Input: s = "OUZODYXAZV", t = "XYZ"

Output: "YXAZ"
Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

Example 2:

Input: s = "xyz", t = "xyz"

Output: "xyz"
Example 3:

Input: s = "x", t = "xy"

Output: ""
Constraints:

1 <= s.length <= 1000
1 <= t.length <= 1000
s and t consist of uppercase and lowercase English letters.
"""
from collections import Counter

class Solution:
	def minWindow(self, s: str, t: str) -> str:

		if not t or not s:
			return ""
		
		t_count = Counter(t)
		required = len(t_count)
		l, r = 0, 0
		formed = 0
		window_counts = {}
		ans = float("inf"), None, None

		while r < len(s):
			char = s[r]
			window_counts[char] = window_counts.get(char, 0) + 1
			if char in t_count and window_counts[char] == t_count[char]:
				formed += 1
			while l <= r and formed == required:
				if (r - l + 1) < ans[0]:
					ans = (r - l + 1, l, r)
				window_counts[s[l]] -= 1
				if s[l] in t_count and window_counts[s[l]] < t_count[s[l]]:
					formed -= 1
				l += 1
			r += 1

		if ans[0] == float("inf"):
			return ""
		else:
			return s[ans[1]:ans[2]+1]

def main():
	solution = Solution()
	s = "OUZODYXAZV"
	t = "XYZ"
	result = solution.minWindow(s, t)
	assert(result == "YXAZ")

	s = "xyz"
	t = "xyz"
	result = solution.minWindow(s, t)
	assert(result == "xyz")

	s = "x"
	t = "xy"
	result = solution.minWindow(s, t)
	assert(result == "")
    
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
