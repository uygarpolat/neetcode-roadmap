"""
Sliding Window Maximum

https://neetcode.io/problems/sliding-window-maximum
 
You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

Return a list that contains the maximum element in the window at each step.

Example 1:

Input: nums = [1,2,1,0,4,2,6], k = 3

Output: [2,2,4,4,6]

Explanation: 
Window position            Max
---------------           -----
[1  2  1] 0  4  2  6        2
 1 [2  1  0] 4  2  6        2
 1  2 [1  0  4] 2  6        4
 1  2  1 [0  4  2] 6        4
 1  2  1  0 [4  2  6]       6
Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
1 <= k <= nums.length
"""
from typing import List
from queue import PriorityQueue
	
class Solution:
	def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

		pq = PriorityQueue()
		result = []

		for i in range(k-1):
			pq.put((-nums[i], i))

		for i in range(k-1, len(nums)):
			pq.put((-nums[i], i))
			while True:
				local_max, index = pq.get()
				if i - k + 1 <= index <= i:
					if index != i - k + 1:
						pq.put((local_max, index))
					break
			result.append(-local_max)

		return result

def main():
	solution = Solution()
	nums = [1,2,1,0,4,2,6]
	k = 3
	result = solution.maxSlidingWindow(nums, k)
	print(result)
	assert(result == [2,2,4,4,6])

	print("✅ All tests passed!")
    
if __name__ == "__main__":
    main()
