"""
Daily Temperatures

https://neetcode.io/problems/daily-temperatures

You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

Example 1:

Input: temperatures = [30,38,30,36,35,40,28]

Output: [1,4,1,2,1,0,0]
Example 2:

Input: temperatures = [22,21,20]

Output: [0,0,0]
Constraints:

1 <= temperatures.length <= 1000.
1 <= temperatures[i] <= 100
"""
from typing import List

class Solution:
	def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

		stack = []
		result = [0] * len(temperatures)

		for index, value in enumerate(temperatures):
			while stack and stack[len(stack) - 1][1] < value:
				index_local, value_local = stack.pop()
				result[index_local] = index - index_local
			stack.append((index, value))

		return result
    
def main():
	solution = Solution()
	temperatures = [30,38,30,36,35,40,28]
	result = solution.dailyTemperatures(temperatures)
	assert(result == [1,4,1,2,1,0,0])

	temperatures = [22,21,20]
	result = solution.dailyTemperatures(temperatures)
	assert(result == [0,0,0])

	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
