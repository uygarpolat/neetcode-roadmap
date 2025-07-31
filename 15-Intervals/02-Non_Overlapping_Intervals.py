"""
Non-overlapping Intervals

https://neetcode.io/problems/non-overlapping-intervals?list=neetcode150

Given an array of intervals intervals where intervals[i] = [start_i, end_i], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note: Intervals are non-overlapping even if they have a common point. For example, [1, 3] and [2, 4] are overlapping, but [1, 2] and [2, 3] are non-overlapping.

Example 1:

Input: intervals = [[1,2],[2,4],[1,4]]

Output: 1
Explanation: After [1,4] is removed, the rest of the intervals are non-overlapping.

Example 2:

Input: intervals = [[1,2],[2,4]]

Output: 0
Constraints:

1 <= intervals.length <= 1000
intervals[i].length == 2
-50000 <= starti < endi <= 50000
"""
from typing import List

class Solution:
	def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
		result = 0
		intervals.sort()
		prev_end = intervals[0][1]

		for start, end in intervals[1:]:
			if start >= prev_end:
				prev_end = end
			else:
				result += 1
				prev_end = min(prev_end, end)
		return result

def main():
	solution = Solution()
	assert solution.eraseOverlapIntervals([[1,2],[2,4],[1,4]]) == 1
	assert solution.eraseOverlapIntervals([[1,2],[2,4]]) == 0
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
