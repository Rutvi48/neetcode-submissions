# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        
        if not l2:
            return l1

        sm = l1.val + l2.val

        add = ListNode(sm % 10)
        carry = sm // 10

        nl1 = l1.next
        nl2 = l2.next
        curr = add

        while nl1 and nl2:
            sm = carry + nl1.val + nl2.val
            curr.next = ListNode(sm%10)
            curr = curr.next
            carry = sm // 10

            nl1 = nl1.next
            nl2 = nl2.next

        rem = None
        if not nl1:
            rem = nl2
        else:
            rem = nl1

        while rem:
            sm = carry + rem.val
            curr.next = ListNode(sm%10)
            curr = curr.next
            carry = sm // 10

            rem = rem.next

        if carry != 0:
            curr.next = ListNode(carry)

        return add

