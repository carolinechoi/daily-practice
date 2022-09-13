## Reverse Linked-List
# Given the head of a singly linked list, reverse the list, and return the reversed list.

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
        
        ## starting at the head
        curr = head 
        
        while curr:
            ## store values temporarily so we can move to it later
            next_temp = curr.next 
            
            ## change the pointer to point to the previous node
            curr.next = prev 
            
            ## swap previous node with current node (traversing from left to right!!)
            prev = curr
            curr = next_temp
            
        return prev