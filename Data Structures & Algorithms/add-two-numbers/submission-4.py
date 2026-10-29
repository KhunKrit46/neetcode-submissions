# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = l1.val + l2.val
        carry = result // 10
        root = ListNode(result % 10)
        curr = root
        l1, l2 = l1.next, l2.next
        while l1 and l2:
            result = l1.val + l2.val + carry
            carry = result // 10
            curr.next = ListNode(result % 10)
            curr = curr.next
            l1, l2 = l1.next, l2.next
        if not (l1 or l2) and carry != 0:
            curr.next = ListNode(carry)
            carry = 0
        while l1:
            result = l1.val + carry
            carry = result // 10
            curr.next = ListNode(result % 10)
            curr = curr.next
            l1 = l1.next
        while l2:
            result = l2.val + carry
            carry = result // 10
            curr.next = ListNode(result % 10)
            curr = curr.next
            l2 = l2.next
        if carry != 0:
            curr.next = ListNode(carry)
        return root
        
        

        
        