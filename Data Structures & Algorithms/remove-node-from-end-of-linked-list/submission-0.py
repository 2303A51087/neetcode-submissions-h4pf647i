# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        e=dummy
        s=dummy
        for i in range(n):
            e=e.next
        while e.next:
            s=s.next
            e=e.next
        s.next=s.next.next
        return dummy.next
        