'''
This is another classic linked list problems where you are given a sinlgly linked lined list and told to detect if there
is a cycle in the list.  A cycle is when a node in the linked list links back to a previous node creating a never ending
cycle. 

To do this, you can use a fast and slow pointer approach.  By using a fast and slow pointer where one is moving at
double the speed of the other, it is garunteed that at some point in their iteration, either the fast pointer will reach
the end of the list, OR the slow ans fast pointer will meet.  If the two pointers meet, then it means that there is a
cycle.  
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head.next

        # Remember to check fast and fast.next as looping conditions.  If you do not check for fast.next, there is a
        # chance that your fast pointer will end on a valid node in the end and throw a null pointer error when trying
        # to access node.next during the next iteration of the loop
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next

        return False
        