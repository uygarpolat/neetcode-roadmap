"""
Meeting Rooms II

https://neetcode.io/problems/meeting-schedule-ii?list=neetcode150
 
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8.

Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)

Example 2:

Input: intervals = [(4,9)]

Output: 1
Constraints:

0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
"""
from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
	def minMeetingRooms(self, intervals: List[Interval]) -> int:

		starts = []
		ends = []
		for interval in intervals:
			starts.append(interval.start)
			ends.append(interval.end)
		starts.sort()
		ends.sort()
        
		res = count = s = e = 0

		while s < len(intervals):
			if starts[s] < ends[e]:
				s += 1
				count += 1
			else:
				e += 1
				count -= 1
			res = max(res, count)
		return res


def main():
	solution = Solution()
	assert solution.minMeetingRooms([Interval(0,40),Interval(5,10),Interval(15,20)]) == 2
	assert solution.minMeetingRooms([Interval(4,9)]) == 1
	assert solution.minMeetingRooms([Interval(1,5),Interval(2,6),Interval(3,7),Interval(4,8),Interval(5,9)]) == 4
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
