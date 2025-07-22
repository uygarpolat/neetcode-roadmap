"""
Reconstruct Flight Path

https://neetcode.io/problems/reconstruct-flight-path?list=neetcode150
 
You are given a list of flight tickets tickets where tickets[i] = [from_i, to_i] represent the source airport and the destination airport.

Each from_i and to_i consists of three uppercase English letters.

Reconstruct the itinerary in order and return it.

All of the tickets belong to someone who originally departed from "JFK". Your objective is to reconstruct the flight path that this person took, assuming each ticket was used exactly once.

If there are multiple valid flight paths, return the lexicographically smallest one.

For example, the itinerary ["JFK", "SEA"] has a smaller lexical order than ["JFK", "SFO"].
You may assume all the tickets form at least one valid flight path.

Example 1:

Input: tickets = [["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]

Output: ["JFK","BUF","HOU","SEA"]
Example 2:

Input: tickets = [["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]

Output: ["JFK","HOU","JFK","SEA","JFK"]
Explanation: Another possible reconstruction is ["JFK","SEA","JFK","HOU","JFK"] but it is lexicographically larger.

Constraints:

1 <= tickets.length <= 300
from_i != to_i
"""
from typing import List

class Solution:
	def findItinerary(self, tickets: List[List[str]]) -> List[str]:

		result = []
		itinerary = {}

		def dfs(source):
			while source in itinerary and itinerary[source]:
				destination = itinerary[source].pop(0)
				dfs(destination)
			result.append(source)

		for source, destination in tickets:
			if source not in itinerary:
				itinerary[source] = []
			itinerary[source].append(destination)

		for source in itinerary:
			itinerary[source].sort()

		dfs("JFK")		
		return result[::-1]

def main():
	solution = Solution()
	assert solution.findItinerary([["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]) == ["JFK","BUF","HOU","SEA"]
	assert solution.findItinerary([["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]) == ["JFK","HOU","JFK","SEA","JFK"]
	assert solution.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]) == ["JFK","NRT","JFK","KUL"]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
