# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def count_nodes(node):
            temp_node = head
            length = 0
            while temp_node is not None:
                temp_node = temp_node.next
                length += 1
            return length    

        
        def reverse_segment(head, k):
            current_node = head
            prev_node = None
            while k>0:
                next_node = current_node.next
                current_node.next = prev_node
                prev_node = current_node
                current_node = next_node
                k -= 1
            return prev_node

        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        length = count_nodes(head)

        while length >= k:
            group_start = prev_group_end.next
            group_end = group_start       