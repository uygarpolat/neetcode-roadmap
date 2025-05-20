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
        return 0
    
def main():
    solution = Solution()
    height = [0,2,0,3,1,0,1,3,2,1]
    result = solution.trap(height)
    assert(height == 9)
    
if __name__ == "__main__":
    main()
