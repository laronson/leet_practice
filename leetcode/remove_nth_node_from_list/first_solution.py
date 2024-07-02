'''
This solution works but it is not optimal.  First off, we need to loop through the linked list twice, first to get the
amount of nodes in the list, then to position ourselves at the node we are going to remove from the list n nodes away
from the head of the list.  Second, we need to add explicit conditionals for cases when the list only contains one node
or when we are trying to remove the head of the list (aka n == node_count).
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Treat counts as len() the return is not zero indexed.  Therefore, we need to start at 1 if we set curr_node to 
        # head
        curr_node, node_count = head,1
        while curr_node.next:
            node_count += 1
            curr_node = curr_node.next

        if node_count == 1:
            return None
        if node_count == n:
            return head.next
        
        curr_node = head
        prev_node = None
        for i in range(node_count-n):
            prev_node = curr_node
            curr_node = curr_node.next

        prev_node.next = getattr(curr_node, 'next')
        
        return head
        

        
