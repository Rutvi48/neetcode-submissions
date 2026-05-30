# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevPtr = None
        nextPtr = None
        currentPtr = head

        while currentPtr and currentPtr.next:
            nextPtr = currentPtr.next
            currentPtr.next = prevPtr
            prevPtr = currentPtr
            currentPtr =  nextPtr

        if currentPtr:
            currentPtr.next = prevPtr

        return currentPtr