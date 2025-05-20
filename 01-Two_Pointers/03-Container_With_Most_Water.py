"""
Container With Most Water
 
You are given an integer array heights where heights[i] represents the height of the i-th bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:

Input: height = [1,7,2,5,4,7,3,6]

Output: 36
Example 2:

Input: height = [2,2,2]

Output: 4
Constraints:

2 <= height.length <= 1000
0 <= height[i] <= 1000
"""
from typing import List

class Solution:
	def maxArea(self, heights: List[int]) -> int:
        
		max_vol = 0
		left = 0
		right = len(heights)-1

		while left < right:
			curr_vol = (right-left) * min(heights[left], heights[right])
			if max_vol < curr_vol:
				max_vol = curr_vol
			if heights[left] < heights[right]:
				left += 1
			else:
				right -= 1
		return max_vol
    
def main():
	solution = Solution()
	height = [1,7,2,5,4,7,3,6]
	result = solution.maxArea(height)
	assert(result == 36)
    
	height = [2,2,2]
	result = solution.maxArea(height)
	assert(result == 4)

	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
