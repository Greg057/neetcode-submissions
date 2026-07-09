# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = ListNode(0, head)
        slow = head
        length = 0
        while slow:
            length += 1
            slow = slow.next
        
        temp = head
        while length - n - 1 > 0:
            temp = temp.next
            length -= 1

        temp.next = temp.next.next
        return head.next

    