# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        The key insight in Floyd's Tortoise and Hare algorithm is that 
        the distance between the starting node and the cycle start node, 
        and the distance between the meeting point and the cycle start node, are equal. 
        This is why resetting one pointer to the head of the list and moving both pointers 
        at the same speed ensures that they will meet at the cycle start node.
        '''
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None


        pointer1 = head
        pointer2 = slow

        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        return pointer1       