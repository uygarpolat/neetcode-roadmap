"""
Largest Rectangle In Histogram

https://neetcode.io/problems/largest-rectangle-in-histogram

You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

Return the area of the largest rectangle that can be formed among the bars.

Note: This chart is known as a histogram.

Example 1:

Input: heights = [7,1,7,2,2,4]

Output: 8
Example 2:

Input: heights = [1,3,7]

Output: 7
Constraints:

1 <= heights.length <= 1000.
0 <= heights[i] <= 1000
"""
from typing import List

class Solution:
	def largestRectangleArea(self, heights: List[int]) -> int:
		
		stack = []
		max_area = 0

		for i, h in enumerate(heights):

			start = i

			while stack and stack[len(stack)-1][1] > h:
				index, height = stack.pop()
				max_area = max(max_area, height * (i - index))
				start = index

			stack.append((start, h))

		for i, h in stack:
			max_area = max(max_area, h * (len(heights) - i))

		return max_area

def main():
	solution = Solution()
	heights = [7,1,7,2,2,4]
	result = solution.largestRectangleArea(heights)
	assert(result == 8)

	heights = [1,3,7]
	result = solution.largestRectangleArea(heights)
	assert(result == 7)

	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
