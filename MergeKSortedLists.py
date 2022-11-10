# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1:
            mergedList = []
            left = 0
            while left < len(lists):
                list1 = lists[left]
                list2 = lists[left + 1] if (left + 1) < len(lists) else None
                left += 2
                mergedList.append(self.mergeTwo(list1, list2))
            lists = mergedList
        return lists[0]

    def mergeTwo(self, list1, list2):
        dummy = ListNode()
        head = dummy
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next

        if list1:
            head.next = list1
        elif list2:
            head.next = list2
        return dummy.next
