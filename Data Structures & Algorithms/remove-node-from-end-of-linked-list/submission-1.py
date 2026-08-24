# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        #length of ll
        length = 0
        while curr:
            length += 1
            curr = curr.next
        #walk to the position behind the node we want to remove
        dummy = ListNode()
        dummy.next = head
        h1 = dummy
        for i in range(length - n):
            h1 = h1.next
        h1.next = h1.next.next
        return dummy.next