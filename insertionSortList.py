# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = head, head.next
        dummy = ListNode(0, head)
        
        while curr:
            if curr.val >= prev.val:
                prev, curr = curr, curr.next
                continue
            start = dummy
            while curr.val > start.next.val:
                start = start.next
            prev.next = curr.next
            curr.next = start.next
            start.next = curr
            curr = prev.next
        return head
            
        