"""
Reverse Linked List

https://neetcode.io/problems/reverse-a-linked-list

Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:

Input: head = [0,1,2,3]

Output: [3,2,1,0]
Example 2:

Input: head = []

Output: []
Constraints:

0 <= The length of the list <= 1000.
-1000 <= Node.val <= 1000
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
	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		prev = None
		curr = head
		while curr:
			nxt = curr.next
			curr.next = prev
			prev = curr
			curr = nxt
		return prev

def main():
	solution = Solution()
     
	head = build_linked_list([0,1,2,3])
	reversed_head = solution.reverseList(head)
	output = linked_list_to_list(reversed_head)
	assert output == [3,2,1,0]

	head = build_linked_list([])
	reversed_head = solution.reverseList(head)
	output = linked_list_to_list(reversed_head)
	assert output == []
 
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
