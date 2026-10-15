# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # For each Node, you reappoint the .next to the previous node. The head becomes the tail 
        # so it will point to null. The tail will become the head so it will point to the previous node
        # But how can this be achieved without losing an entire section of the link? A temp variable?
        # [data1] ---> [data2] ---> [data3]

        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev