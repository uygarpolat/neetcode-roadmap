"""
Linked List Cycle Detection

https://neetcode.io/problems/linked-list-cycle-detection

Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.

Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.

Note: index is not given to you as a parameter.

Example 1:

Input: head = [1,2,3,4], index = 1

Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:

Input: head = [1,2], index = -1

Output: false
Constraints:

1 <= Length of the list <= 1000.
-1000 <= Node.val <= 1000
index is -1 or a valid index in the linked list.
"""
from typing import Optional

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
        
def build_linked_list(vals: list[int]) -> Optional[ListNode]:
	dummy = ListNode()
	curr = dummy
	for v in vals:
		curr.next = ListNode(v)
		curr = curr.next
	return dummy.next

class Solution:
	def hasCycle(self, head: Optional[ListNode]) -> bool:
		head1 = head.next
		head2 = head
		counter = 0
		while head1 and head2:
			if head1.val == head2.val:
				return True
			head1 = head1.next
			if counter % 2 == 0:
				head2 = head2.next	
			counter += 1
		return False
	
def main():
	solution = Solution()
     
	head = build_linked_list([1,2,3,4])
	cycle_detector = solution.hasCycle(head)
	assert cycle_detector == False

	head = build_linked_list([1,2])
	cycle_detector = solution.hasCycle(head)
	assert cycle_detector == False
 
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
