# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        c1 = l1
        c2 = l2
        res = ListNode(0)
        current = res
        carry = 0

        while c1 is not None or c2 is not None:
            v1 = 0 if c1 is None else c1.val
            v2 = 0 if c2 is None else c2.val
            temp = (v1 + v2 + carry)
            carry = temp // 10
            current.next = ListNode(temp % 10)

            if c2 is not None:
                c2 = c2.next
            if c1 is not None:
                c1 = c1.next
            current = current.next

        if carry > 0:
            current.next = ListNode(carry)
        return res.next
