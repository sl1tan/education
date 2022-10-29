# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len = 0
        last = head
        while (1):
            if last.next == None:
                len += 1
                break
            last = last.next
            len += 1

        count = 0
        middle = len // 2
        last = head
        while 1:
            if last.next == None:
                return head
            last = last.next
            count += 1
            if count == middle:
                break
        return last
