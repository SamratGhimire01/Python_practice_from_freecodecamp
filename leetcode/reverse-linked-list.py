# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next  # Save the rest of the list
            curr.next = prev       # Flip the pointer backward
            prev = curr            # Move prev forward
            curr = next_node       # Move curr forward
            
        return prev  # Prev is the new head of the reversed list
# Example usage:
# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# solution = Solution()
# reversed_head = solution.reverseList(head)
# while reversed_head:
#     print(reversed_head.val)  