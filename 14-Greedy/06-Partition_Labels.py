"""
Partition Labels

https://neetcode.io/problems/partition-labels?list=neetcode150

You are given a string s consisting of lowercase english letters.

We want to split the string into as many substrings as possible, while ensuring that each letter appears in at most one substring.

Return a list of integers representing the size of these substrings in the order they appear in the string.

Example 1:

Input: s = "xyxxyzbzbbisl"

Output: [5, 5, 1, 1, 1]
Explanation: The string can be split into ["xyxxy", "zbzbb", "i", "s", "l"].

Example 2:

Input: s = "abcabc"

Output: [6]
Constraints:

1 <= s.length <= 100
"""
from typing import List
from collections import defaultdict

class Solution:
	def partitionLabels(self, s: str) -> List[int]:

		book = defaultdict(int)
		result = []

		for c in s:
			book[c] += 1

		counter = 0
		size = 1

		for c in s:
			counter += book[c]
			if counter == 1:
				result.append(size)
				size = 0
			book[c] = 0
			counter -= 1
			size += 1

		return result

def main():
	solution = Solution()
	assert solution.partitionLabels("xyxxyzbzbbisl") == [5, 5, 1, 1, 1]
	assert solution.partitionLabels("abcabc") == [6]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
