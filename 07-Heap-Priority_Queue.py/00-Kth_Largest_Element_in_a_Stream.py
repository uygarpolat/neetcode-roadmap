"""
Kth Largest Element in a Stream

https://neetcode.io/problems/kth-largest-integer-in-a-stream?list=neetcode150

Design a class to find the kth largest integer in a stream of values, including duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.

Implement the following methods:

constructor(int k, int[] nums) Initializes the object given an integer k and the stream of integers nums.
int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.
Example 1:

Input:
["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]

Output:
[null, 3, 3, 3, 5, 6]

Explanation:
KthLargest kthLargest = new KthLargest(3, [1, 2, 3, 3]);
kthLargest.add(3);   // return 3
kthLargest.add(5);   // return 3
kthLargest.add(6);   // return 3
kthLargest.add(7);   // return 5
kthLargest.add(8);   // return 6
Constraints:

1 <= k <= 1000
0 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-1000 <= val <= 1000
There will always be at least k integers in the stream when you search for the kth integer.
"""
from typing import List
import heapq

class KthLargest:

	def __init__(self, k: int, nums: List[int]):
		self.k = k
		self.hq = nums
		heapq.heapify(self.hq)
		while len(self.hq) > k:
			heapq.heappop(self.hq)
        
	def add(self, val: int) -> int:
		if len(self.hq) < self.k:
			heapq.heappush(self.hq, val)
		elif val > self.hq[0]:
			heapq.heapreplace(self.hq, val)
		return self.hq[0]

def main():
	kthLargest = KthLargest(3, [1, 2, 3, 3])
	assert kthLargest.add(3) == 3
	assert kthLargest.add(5) == 3
	assert kthLargest.add(6) == 3
	assert kthLargest.add(7) == 5
	assert kthLargest.add(8) == 6
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
