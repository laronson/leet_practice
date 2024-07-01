'''
This problem presented a single directed linked list and asked us to reorder it using the formula: with variable n as
the length of the linked list, transform the list to be in the format [l[0], l[n-1], l[1], l[n-2]...].

To solve this problem, you first needed to draw out what that reordering looked like.  Once you do that, you can see
that the reordering, from a human pount of view, is taking the last element in the list and then inserting it after the
first element in the list.  Then, if the list is long enough, take the second to last element in the list and slide it
in between the second and third elements in the array ect...  What we need to do is to perform that reordering in our
code.  At first I thought I would be able to use a two pointer approach where I had a pointer at the begining of the
lsit and then another pointer at the end.  However, because the linked list was only singly linked and you could not go
backwards, the rightmost pointer would be useless.  Therefore, I decided to split the list, reverse the second half so I
could iterathe thought it in a forward motion and then start to perform the reorder.

To conquer this programatically, I broke this problem up into three parts:
1) Find the middle of the linked list use a fast and slow pointer approach.  To do this, put a slow and fast pointer at
head and head.next in the list respectively.  Then iterate until the fast pointer reaches the end of the list.  This
will naturally place slow at the middle of list because fast is moving doubly as fast though the list as slow is.
2) Split and reorder the second half of the list found in part one.  This is just a normal linked list reorder, however,
you need to remember to cut off the head of your list your are reordering because if you do not, it will still be
attached to the first half of the list that you do not want to reverse.
3) Perform the merging and reordering logic and then return the head of the linked list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import ceil
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse second half
        curr_node = slow.next
        #THIS IS IMPORTANT,
        #Slow is still connected to rest of the linked list and we only want to reverse half of the list
        #Therefore, we must reset slow.next to null to cut it off from the rest of the list before we reverse it
        prev_node = slow.next = None
        while curr_node:
            tmp = curr_node.next
            curr_node.next = prev_node
            prev_node=curr_node
            curr_node = tmp

        
        first_half, second_half = head, prev_node
        while second_half:
            tmp_first,tmp_second = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = tmp_first
            first_half = tmp_first
            second_half = tmp_second

        return head


        

