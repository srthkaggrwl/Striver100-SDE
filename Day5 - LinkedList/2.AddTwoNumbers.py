# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:

            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

            total = value1 + value2 + carry
            carry = total // 10
            new_value = total % 10

            current.next = ListNode(new_value)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next


        return dummy.next



solution = Solution()
l1 = [2,4,3]
l2 = [5,6,4]
solution.addTwoNumbers(l1, l2)        
        