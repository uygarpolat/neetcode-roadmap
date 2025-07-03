from typing import List
from collections import defaultdict
import heapq

class Twitter:

	def __init__(self):
		self.count = 0
		self.tweetMap = defaultdict(list)
		self.followMap = defaultdict(set)

	def postTweet(self, userId: int, tweetId: int) -> None:
		self.tweetMap[userId].append([self.count, tweetId])
		self.count -= 1

	def getNewsFeed(self, userId: int) -> List[int]:
		res = []
		minHeap = []

		self.followMap[userId].add(userId)
		for followeeId in self.followMap[userId]:
			if followeeId in self.tweetMap:
				index = len(self.tweetMap[followeeId]) - 1
				count, tweetId = self.tweetMap[followeeId][index]
				heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

		while minHeap and len(res) < 10:
			count, tweetId, followeeId, index = heapq.heappop(minHeap)
			res.append(tweetId)
			if index >= 0:
				count, tweetId = self.tweetMap[followeeId][index]
				heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
		return res
        
	def follow(self, followerId: int, followeeId: int) -> None:
		self.followMap[followerId].add(followeeId)

	def unfollow(self, followerId: int, followeeId: int) -> None:
		self.followMap[followerId].discard(followeeId)
        
def main():
	twitter = Twitter();
	twitter.postTweet(1, 10)
	twitter.postTweet(2, 20)
	assert twitter.getNewsFeed(1) == [10]
	assert twitter.getNewsFeed(2) == [20]
	twitter.follow(1, 2)
	assert twitter.getNewsFeed(1) ==  [20, 10]
	assert twitter.getNewsFeed(2) == [20]
	twitter.unfollow(1, 2)
	assert twitter.getNewsFeed(1) == [10]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
