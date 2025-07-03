"""
Find Median From Data Stream

https://neetcode.io/problems/find-median-in-a-data-stream?list=neetcode150

The median is the middle value in a sorted list of integers. For lists of even length, there is no middle value, so the median is the mean of the two middle values.

For example:

For arr = [1,2,3], the median is 2.
For arr = [1,2], the median is (1 + 2) / 2 = 1.5
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far.
Example 1:

Input:
["MedianFinder", "addNum", "1", "findMedian", "addNum", "3" "findMedian", "addNum", "2", "findMedian"]

Output:
[null, null, 1.0, null, 2.0, null, 2.0]

Explanation:
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.findMedian(); // return 1.0
medianFinder.addNum(3);    // arr = [1, 3]
medianFinder.findMedian(); // return 2.0
medianFinder.addNum(2);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
Constraints:

-100,000 <= num <= 100,000
findMedian will only be called after adding at least one integer to the data structure.
"""
import heapq

class MedianFinder:

	def __init__(self):
		self.minHeap = []
		self.maxHeap = []
		heapq.heapify(self.minHeap)
		heapq.heapify(self.maxHeap)
        
	def addNum(self, num: int) -> None:
		if not self.minHeap:
			heapq.heappush(self.minHeap, num)
		elif num > self.minHeap[0]:
			heapq.heappush(self.minHeap, num)
		else:
			heapq.heappush(self.maxHeap, -num)

		if len(self.minHeap) - len(self.maxHeap) > 1:
			heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
		elif len(self.maxHeap) - len(self.minHeap)> 1:
			heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

	def findMedian(self) -> float:
		if len(self.maxHeap) > len(self.minHeap):
			return -self.maxHeap[0]
		elif len(self.maxHeap) < len(self.minHeap):
			return self.minHeap[0]
		else:
			return (self.minHeap[0] - self.maxHeap[0]) / 2
		
def main():
	medianFinder = MedianFinder()
	medianFinder.addNum(1)
	assert medianFinder.findMedian() == 1.0
	medianFinder.addNum(3)
	assert medianFinder.findMedian() == 2.0
	medianFinder.addNum(2)
	assert medianFinder.findMedian() == 2.0 or print(medianFinder.findMedian()) or False
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
