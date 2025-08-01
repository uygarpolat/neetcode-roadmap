"""
Minimum Interval to Include Each Query

https://neetcode.io/problems/minimum-interval-including-query?list=neetcode150

You are given a 2D integer array intervals, where intervals[i] = [left_i, right_i] represents the ith interval starting at left_i and ending at right_i (inclusive).

You are also given an integer array of query points queries. The result of query[j] is the length of the shortest interval i such that left_i <= queries[j] <= right_i. If no such interval exists, the result of this query is -1.

Return an array output where output[j] is the result of query[j].

Note: The length of an interval is calculated as right_i - left_i + 1.

Example 1:

Input: intervals = [[1,3],[2,3],[3,7],[6,6]], queries = [2,3,1,7,6,8]

Output: [2,2,3,5,1,-1]
Explanation:

Query = 2: The interval [2,3] is the smallest one containing 2, it's length is 2.
Query = 3: The interval [2,3] is the smallest one containing 3, it's length is 2.
Query = 1: The interval [1,3] is the smallest one containing 1, it's length is 3.
Query = 7: The interval [3,7] is the smallest one containing 7, it's length is 5.
Query = 6: The interval [6,6] is the smallest one containing 6, it's length is 1.
Query = 8: There is no interval containing 8.
Constraints:

1 <= intervals.length <= 1000
1 <= queries.length <= 1000
1 <= left_i <= right_i <= 10000
1 <= queries[j] <= 10000
"""
from typing import List
import heapq

class Solution:
	def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

		intervals.sort()
		n = len(intervals)
		result = {}
		hq = []
		heapq.heapify(hq)

		i = 0
		for query in sorted(queries):
			while i < n and intervals[i][0] <= query:
				l, r = intervals[i]
				heapq.heappush(hq, (r-l+1, r))
				i += 1

			while hq and hq[0][1] < query:
				heapq.heappop(hq)
			result[query] = hq[0][0] if hq else -1
		return[result[q] for q in queries]

def main():
	solution = Solution()
	assert solution.minInterval([[1,3],[2,3],[3,7],[6,6]], [2,3,1,7,6,8]) == [2,2,3,5,1,-1]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
