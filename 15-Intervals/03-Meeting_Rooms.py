"""
Meeting Rooms

https://neetcode.io/problems/meeting-schedule?list=neetcode150
 
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

Example 1:

Input: intervals = [(0,30),(5,10),(15,20)]

Output: false
Explanation:

(0,30) and (5,10) will conflict
(0,30) and (15,20) will conflict
Example 2:

Input: intervals = [(5,8),(9,15)]

Output: true
Note:

(0,8),(8,10) is not considered a conflict at 8
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
	def canAttendMeetings(self, intervals: List[Interval]) -> bool:

		if not intervals:
			return True

		intervals.sort(key=lambda x: x.start)

		prev_end = intervals[0].end

		for interval in intervals[1:]:
			start, end = interval.start, interval.end
			if start < prev_end:
				return False
			prev_end = end
		return True

def main():
	solution = Solution()
	assert solution.canAttendMeetings([Interval(0,30),Interval(5,10),Interval(15,20)]) == False
	assert solution.canAttendMeetings([Interval(5,8),Interval(9,15)]) == True
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
