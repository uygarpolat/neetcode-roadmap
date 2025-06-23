"""
Remove Node From End of Linked List

https://neetcode.io/problems/remove-node-from-end-of-linked-list

You are given the beginning of a linked list head, and an integer n.

Remove the nth node from the end of the list and return the beginning of the list.

Example 1:

Input: head = [1,2,3,4], n = 2

Output: [1,2,4]
Example 2:

Input: head = [5], n = 1

Output: []
Example 3:

Input: head = [1,2], n = 2

Output: [2]
Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
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
	def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
		dummy = ListNode(0, head)
		head1 = dummy
		head2 = dummy

		for _ in range(n+1):
			head1 = head1.next

		while head1:
			head1 = head1.next
			head2 = head2.next

		head2.next = head2.next.next

		return dummy.next

def main():
	solution = Solution()
     
	head = build_linked_list([1,2,3,4])
	removed_head = solution.removeNthFromEnd(head, 2)
	output = linked_list_to_list(removed_head)
	assert output == [1,2,4] or print(output) or False

	head = build_linked_list([5])
	removed_head = solution.removeNthFromEnd(head, 1)
	output = linked_list_to_list(removed_head)
	assert output == []

	head = build_linked_list([1,2])
	removed_head = solution.removeNthFromEnd(head, 2)
	output = linked_list_to_list(removed_head)
	assert output == [2]
 
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
