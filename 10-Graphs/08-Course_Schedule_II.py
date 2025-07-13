"""
Course Schedule II

https://neetcode.io/problems/course-schedule-ii?list=neetcode150

You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

Return a valid ordering of courses you can take to finish all courses. If there are many valid answers, return any of them. If it's not possible to finish all courses, return an empty array.

Example 1:

Input: numCourses = 3, prerequisites = [[1,0]]

Output: [0,1,2]
Explanation: We must ensure that course 0 is taken before course 1.

Example 2:

Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]

Output: []
Explanation: It's impossible to finish all courses.

Constraints:

1 <= numCourses <= 1000
0 <= prerequisites.length <= 1000
All prerequisite pairs are unique.
"""
from typing import List
from collections import defaultdict, deque

class Solution:
	def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
            
		coursework = defaultdict(list)
		indegree = [0] * numCourses


		for course, prerequisite in prerequisites:
			coursework[course].append(prerequisite)
			indegree[prerequisite] += 1

		dq = deque()
		for n in range(numCourses):
			if indegree[n] == 0:
				dq.append(n)

		result = 0
		output = []

		while dq:
			currentCourse = dq.popleft()
			output.append(currentCourse)
			result += 1
			for prerequisite in coursework[currentCourse]:
				indegree[prerequisite] -= 1
				if indegree[prerequisite] == 0:
					dq.append(prerequisite)

		if result == numCourses:
			return output[::-1]
		return []


def main():
	solution = Solution()
	assert solution.findOrder(3, [[1,0]]) == [0,2,1]
	assert solution.findOrder(3, [[0,1],[1,2],[2,0]]) == []
	print("✅ All tests passed!")

if __name__ == "__main__":
    main()
