# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        dummy = ListNode()
        dummy.next = head

        first_pointer = dummy
        second_pointer = dummy

        for _ in range(n+1):
            first_pointer = first_pointer.next


        while first_pointer:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next

        popped_node = second_pointer.next
        second_pointer.next = popped_node.next
        popped_node.next = None

        return dummy.next           
