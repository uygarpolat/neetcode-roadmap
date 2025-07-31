"""
Merge Intervals

https://neetcode.io/problems/merge-intervals?list=neetcode150

Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

You may return the answer in any order.

Note: Intervals are non-overlapping if they have no common point. For example, [1, 2] and [3, 4] are non-overlapping, but [1, 2] and [2, 3] are overlapping.

Example 1:

Input: intervals = [[1,3],[1,5],[6,7]]

Output: [[1,5],[6,7]]
Example 2:

Input: intervals = [[1,2],[2,3]]

Output: [[1,3]]
Constraints:

1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= start <= end <= 1000
"""
from typing import List

class Solution:
	def merge(self, intervals: List[List[int]]) -> List[List[int]]:

		intervals.sort()
		result = []		

		for start, end in intervals:
			if not result or result[-1][1] < start:
				result.append([start,end])
			else:
				result[-1][1] = max(end, result[-1][1])

		return result

def main():
	solution = Solution()
	assert solution.merge([[1,3],[1,5],[6,7]]) == [[1,5],[6,7]]
	assert solution.merge([[1,2],[2,3]]) == [[1,3]]
	assert solution.merge([[1,4],[2,3]]) == [[1,4]]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
