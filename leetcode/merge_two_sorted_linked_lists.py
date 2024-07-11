'''
This is a classic (easy-level) linked list problem where you are given two linked lists sorted in ascending order.  You
are tasekd with merging these two linked lists making sure that the resulting merged list maintains its nodes in
ascending order.

To do this, I first created a "dummy node" which will be used as the head of our linked list.  To make sure we can
access the head of this linked list after adding all of the merged elements, we also save this in a seperate variable
titled "pre_merged_head".  This variable will be used in the return statement to make sure we return the front of the
merged linked list.  

To actually merge the two lists, we loop throgh each list until we have iterated through all of one of the lists.  For
each iteration, we check to see if the value at the current position in linked list 1 or linked list 2 is less than the
other.  The one that has the lesser value is inserted into the list.  It is important that we use the lesser than symbol
here because we are inserting the value at the right most side of the list meaning that we want all values that have
greater value to go later (further to the right) in the sorted merged list.  Once we have finished iterating through one
of the lists, we know that if there are any elements remaining in the other list that they are greater than any element
that we have inserted into the merged list so far.  Therefore, we can simply insert the rest of the remaining list at
the end of the merged list  d.
'''

        name = laronson
        email = leonard.aronson@wearstrive.com


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        pre_merged_head = dummy

        while list1 and list2:
            # We need to use a less than or equal to comparison here because we want to insert the values 
            # have the lesser value first.  If we wanted to merge in decending order, then we could do the opposite
            if list1.val <= list2.val:
                dummy.next = list1
                dummy = dummy.next
                list1 = list1.next
            else:
                dummy.next = list2
                dummy = dummy.next
                list2 = list2.next
        
        # Could use this structure for if statements, but you could use what is below for a more condenced
        # version
        # if list1:
        #     dummy.next = list1
        # elif list2: 
        #     dummy.next = list2
        dummy.next = list1 or list2

        return pre_merged_head.next


                
            


                