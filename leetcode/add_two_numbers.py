'''
This problem presents us with two linked lists which are list representations of numbers printed in reverse order.  For
example, the number 123 would be represented by the linked list [3,2,1] where the singles digit is the first element in
the list and the hundreds digit is the last element.  The problem asks us to add the numbers represented by the linked
list nd return the sum as a linked list representation in the same form as the input lists (aka in reversed order).

To do this problem, we iterate through each linked list node by node adding the values of the nodes that are in the same
digits place.  For example if we were to add the numbers 10 (represented by [0,1]) and 20 (represented by [0,2]), we
would first add 0 + 0 in the singles digit place and then 1 + 2 in the tens digit place.  As we iterate through and add
those numbers, we can add the sum values to a new linked list which, if we add in the order from left to right of the
input lists, would naturally be in the format of the input lists.  The other thing we need to do is consider carryover.
If there is carryover (aka the digits from each node sum to a number that is greater than ten) we need to make sure we
account for that when summing the digits in the next digit slot.  Lastly, we need to be concerned with the case where
one list has more digits than the other (aka there are more nodes in one of the lists).  Because of that, we need to
check if the nodes exist before accessing .val or .next on each node.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_curr, l2_curr, carry_over = l1, l2, 0
        dummy_sum = ListNode(-1, None)

        sum_list = dummy_sum
        while l1_curr or l2_curr:
            v1 = l1_curr.val if l1_curr else 0 
            v2 = l2_curr.val if l2_curr else 0 

            node_sum = v1 + v2 + carry_over
            carry_over = 1 if node_sum // 10 > 0 else 0
            digit = node_sum % 10
            sum_list.next = ListNode(digit)

            sum_list = sum_list.next
            l1_curr = l1_curr.next if l1_curr else None
            l2_curr = l2_curr.next if l2_curr else None
        
        if carry_over == 1:
            sum_list.next = ListNode(1, None)

        
        return dummy_sum.next


        