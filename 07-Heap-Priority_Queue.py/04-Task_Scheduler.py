"""
Task Scheduler

https://neetcode.io/problems/task-scheduling?list=neetcode150

You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.

Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.

The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.

Return the minimum number of CPU cycles required to complete all tasks.

Example 1:

Input: tasks = ["X","X","Y","Y"], n = 2

Output: 5
Explanation: A possible sequence is: X -> Y -> idle -> X -> Y.

Example 2:

Input: tasks = ["A","A","A","B","C"], n = 3

Output: 9
Explanation: A possible sequence is: A -> B -> C -> Idle -> A -> Idle -> Idle -> Idle -> A.

Constraints:

1 <= tasks.length <= 1000
0 <= n <= 100
"""
from typing import List
import heapq
from collections import deque

class Solution:
	def leastInterval(self, tasks: List[str], n: int) -> int:
		book = [0] * 26
		hq = []
		heapq.heapify(hq)

		for task in tasks:
			index = ord(task) - ord("A")
			book[index] += 1

		for task in book:
			if task != 0:
				heapq.heappush(hq, -task)
		
		time = 0
		q = deque()

		while hq or q:
			time += 1

			if hq:
				biggest = -heapq.heappop(hq)
				new_biggest = biggest - 1
				if new_biggest != 0:
					q.append([-new_biggest, time + n])
			else:
				time = q[0][1]

			if q and q[0][1] == time:
				heapq.heappush(hq, q.popleft()[0])

		return time
	
def main():
	solution = Solution()
	assert solution.leastInterval(["X","X","Y","Y"], 2) == 5
	assert solution.leastInterval(["A","A","A","B","C"], 3) == 9
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
