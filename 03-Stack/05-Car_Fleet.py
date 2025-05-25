"""
Car Fleet

https://neetcode.io/problems/car-fleet
 
There are n cars traveling to the same destination on a one-lane highway.

You are given two arrays of integers position and speed, both of length n.

position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)
The destination is at position target miles.

A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination.

Example 1:

Input: target = 10, position = [1,4], speed = [3,2]

Output: 1
Explanation: The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet, meeting each other at 10, the destination.

Example 2:

Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

Output: 3
Explanation: The cars starting at 4 and 7 become a fleet at position 10. The cars starting at 1 and 0 never catch up to the car ahead of them. Thus, there are 3 car fleets that will arrive at the destination.

Constraints:

n == position.length == speed.length.
1 <= n <= 1000
0 < target <= 1000
0 < speed[i] <= 100
0 <= position[i] < target
All the values of position are unique.
"""
from typing import List

class Solution:
	def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

		joint_info = list(zip(position, speed))
		joint_info.sort(reverse=True)
		stack = []

		for i in range(len(joint_info)):
			position_i, speed_i = joint_info[i][0], joint_info[i][1]
			time_i = (target - position_i) / speed_i
			if not stack:
				stack.append(time_i)
			else:
				if time_i > stack[-1]:
					stack.append(time_i)

		return len(stack)

def main():
	solution = Solution()
	target = 10
	position = [1,4]
	speed = [3,2]
	result = solution.carFleet(target, position, speed)
	assert(result == 1)

	target = 10
	position = [4,1,0,7]
	speed = [2,2,1,1]
	result = solution.carFleet(target, position, speed)
	assert(result == 3)

	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
