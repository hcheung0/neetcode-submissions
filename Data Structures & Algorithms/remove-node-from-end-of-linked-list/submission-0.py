# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # traverse to end of list, keeping track of length w/ an index var
        # move n steps back
        # relink via pointing len-n-1 to len-n+1. change if its end of list or beginning

        curr = head
        length = 0
        
        while curr:
            length += 1
            curr = curr.next
        
        pos = length - n
        curr = head
        prev = 0

        if pos == 0:
            return head.next
        
        while curr:
            prev += 1
            if prev == pos:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head

        
