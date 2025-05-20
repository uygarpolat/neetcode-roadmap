"""
Trapping Rain Water

https://neetcode.io/problems/trapping-rain-water

You are given an array non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.

Example 1:


Input: height = [0,2,0,3,1,0,1,3,2,1]

Output: 9
Constraints:

1 <= height.length <= 1000
0 <= height[i] <= 1000
"""
from typing import List

class Solution:
	def trap(self, height: List[int]) -> int:

		length = len(height)
		prefix = [0] * length
		suffix = [0] * length
		prefix[0] = 0
		suffix[length-1] = 0
		result = 0
        
		for i in range(1, length):
			prefix[i] = max(prefix[i-1], height[i-1])

		for i in range(length-2,-1,-1):
			suffix[i] = max(suffix[i+1], height[i+1])

		for i in range(length):
			result += max(0, min(prefix[i],suffix[i]) - height[i])
             
		return result
    
def main():
	solution = Solution()
	height = [0,2,0,3,1,0,1,3,2,1]
	result = solution.trap(height)
	assert(result == 9)

	print("✅ All tests passed!")
    
if __name__ == "__main__":
    main()
