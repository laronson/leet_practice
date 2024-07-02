'''
This problem presents us with a linked list and asks us to remove an element from the list that is n nodes away from the
end of the list.

First, to understand what the problem is asking, it helped to put the question prompt in terms of what we are trying to
do so we do not mix up the instructions.  What we are trying to do is to remove the node that is n spaces away from the
end of the list.  Do not confuse this with n nodes away from the beginning.

This solution uses two different strategies to accomplish our goal of removing the node n nodes away from the end of the
list.  First, to set up our solution, we must create a dummy node that we can start at to ensure our iterative solution
always includes the head of the list as part of our iterations.  In doing so, we set our left pointer as a new node,
dummy that is a node that points to the head of the list.  Therefore, when we iterate for the first time using the left
pointer, we start on the head of the list.  Second, to find the node we are trying to remove, we use a two pointer
(aka fast and slow pointers) strategy.  We set our left pointer to our dummy node and our right pointer n nodes away
from the left node.  With this setup, if we iterate right to be right.next until it is at the end of the list, the left
pointer will naturally sit at the node n + 1 (n+1 because left is sitting at dummy and not at head) nodes away from the end of the list.    Once there, we can set left.next to be
left.next.next to remove the middle node.  Finally, because we set dummy.next to be the head of the list and, with the
left right pointer strategy, the dummy node will remain up to date if we have to remove the head of the list, we can
return dummy.next as the return of the function

With those two strategies, we ensure a few things.  First, we always remove the correct node.  Second, if we are
removing a node at the beginning or the end of the list, left.node will always exist because after iterating, the left
pointer will always be at the dummy node, at the node to the right of the end of the list, or in between those two
points.  
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left = dummy
        right = dummy.next

        for i in range(n):
            print(i)
            right = right.next
        
        while right:
            right = right.next
            left = left.next

        left.next = left.next.next
        return dummy.next
        