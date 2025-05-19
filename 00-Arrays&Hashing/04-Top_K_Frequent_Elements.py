"""
Top K Frequent Elements
 
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.
"""
from collections import Counter
from typing import List

class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		freq = Counter(nums)
		n = len(nums)
		buckets = [[] for _ in range(n+1)]
		for num, count in freq.items():
			buckets[count].append(num)
		result = []
		for f in range(n, 0, -1):
			for num in buckets[f]:
				result.append(num)
				if len(result) == k:
					return result

def main():
	solution = Solution()
	nums = [1,2,2,3,3,3]
	k = 2
	result = solution.topKFrequent(nums, k)
	print(result) # Expected outcome: [3,2]

	nums = [7,7]
	k = 1
	result = solution.topKFrequent(nums, k)
	print(result) # Expected outcome: [7]

if __name__ == "__main__":
	main()
