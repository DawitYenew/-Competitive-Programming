# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        listNode = ListNode(-1)
        print(listNode)
        listNode.next = head
        fast, slow = head, listNode
        while fast:
            while fast.next and fast.val == fast.next.val:
                fast = fast.next
            if slow.next == fast:
                slow, fast = slow.next, fast.next
            else:
                slow.next = fast.next
                fast = slow.next
                
        return listNode.next
