"""
Reorder Linked List

https://neetcode.io/problems/reorder-linked-list

You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

Example 1:

Input: head = [2,4,6,8]

Output: [2,8,4,6]
Example 2:

Input: head = [2,4,6,8,10]

Output: [2,10,4,8,6]
Constraints:

1 <= Length of the list <= 1000.
1 <= Node.val <= 1000
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
	def reorderList(self, head: ListNode) -> None:
		if not head or not head.next or not head.next.next:
			return
		
		slow, fast = head, head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

		prev, curr = None, slow.next
		slow.next = None
		while curr:
			nxt = curr.next
			curr.next = prev
			prev = curr
			curr = nxt

		p1, p2 = head, prev
		while p2:
			tmp1, tmp2 = p1.next, p2.next
			p1.next = p2
			p2.next = tmp1
			p1, p2 = tmp1, tmp2

def main():
	solution = Solution()

	head = build_linked_list([0,1,2,3,4,5,6])
	solution.reorderList(head)
	reordered_list = linked_list_to_list(head)
	assert reordered_list == [0,6,1,5,2,4,3], reordered_list

	head = build_linked_list([2,4,6,8])
	solution.reorderList(head)
	reordered_list = linked_list_to_list(head)
	assert reordered_list == [2,8,4,6], reordered_list

	head = build_linked_list([2,4,6,8,10])
	solution.reorderList(head)
	reordered_list = linked_list_to_list(head)
	assert reordered_list == [2,10,4,8,6], reordered_list

	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
