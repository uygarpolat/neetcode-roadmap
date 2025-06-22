"""
Time Based Key-Value Store

https://neetcode.io/problems/time-based-key-value-store

Implement a time-based key-value data structure that supports:

Storing multiple values for the same key at specified time stamps
Retrieving the key's value at a specified timestamp
Implement the TimeMap class:

TimeMap() Initializes the object.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns the most recent value of key if set was previously called on it and the most recent timestamp for that key prev_timestamp is less than or equal to the given timestamp (prev_timestamp <= timestamp). If there are no values, it returns "".
Note: For all calls to set, the timestamps are in strictly increasing order.

Example 1:

Input:
["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]

Output:
[null, null, "happy", "happy", null, "sad"]

Explanation:
TimeMap timeMap = new TimeMap();
timeMap.set("alice", "happy", 1);  // store the key "alice" and value "happy" along with timestamp = 1.
timeMap.get("alice", 1);           // return "happy"
timeMap.get("alice", 2);           // return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
timeMap.set("alice", "sad", 3);    // store the key "alice" and value "sad" along with timestamp = 3.
timeMap.get("alice", 3);           // return "sad"
Constraints:

1 <= key.length, value.length <= 100
key and value only include lowercase English letters and digits.
1 <= timestamp <= 1000
"""
class TimeMap:

	def __init__(self):
		self.store = {}

	def set(self, key: str, value: str, timestamp: int) -> None:
		if key not in self.store:
			self.store[key] = []
		self.store[key].append((timestamp, value))

	def get(self, key: str, timestamp: int) -> str:

		if key not in self.store:
			return ""
		
		lo = 0
		hi = len(self.store[key]) - 1
		result = ""

		while lo <= hi:
			mid = (hi + lo) // 2
			prev_timestamp = self.store[key][mid][0]
			if prev_timestamp <= timestamp:
				result = self.store[key][mid][1]
				lo = mid + 1
			else:
				hi = mid - 1
				
		return result
        
def main():
	timeMap = TimeMap()
	timeMap.set("alice", "happy", 1)
	result = timeMap.get("alice", 1)
	assert result == "happy"
	result = timeMap.get("alice", 2)
	assert result == "happy"
	timeMap.set("alice", "sad", 3)
	result = timeMap.get("alice", 3)
	assert result == "sad"
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
