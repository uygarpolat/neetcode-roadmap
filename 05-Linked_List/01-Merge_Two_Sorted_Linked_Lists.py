"""
Merge Two Sorted Linked Lists

https://neetcode.io/problems/linked-list-cycle-detection

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,5]

Output: [1,1,2,3,4,5]
Example 2:

Input: list1 = [], list2 = [1,2]

Output: [1,2]
Example 3:

Input: list1 = [], list2 = []

Output: []
Constraints:

0 <= The length of the each list <= 100.
-100 <= Node.val <= 100
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

def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

class Solution:
	def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
		l1 = list1
		l2 = list2
		dummy = ListNode()
		curr = dummy
		while l1 and l2:
			if l1.val < l2.val:
				curr.next = l1
				l1 = l1.next
			else:
				curr.next = l2
				l2 = l2.next
			curr = curr.next
		curr.next = l1 or l2
		return dummy.next

def main():
	solution = Solution()
     
	head1 = build_linked_list([1,2,4])
	head2 = build_linked_list([1,3,5])
	merged_head = solution.mergeTwoLists(head1, head2)
	output = linked_list_to_list(merged_head)
	assert output == [1,1,2,3,4,5]

	head1 = build_linked_list([])
	head2 = build_linked_list([1,2])
	merged_head = solution.mergeTwoLists(head1, head2)
	output = linked_list_to_list(merged_head)
	assert output == [1,2]

	head1 = build_linked_list([])
	head2 = build_linked_list([])
	merged_head = solution.mergeTwoLists(head1, head2)
	output = linked_list_to_list(merged_head)
	assert output == []

	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
