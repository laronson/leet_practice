'''
This solution may have worked but it had way way too many steps and did not catch the trick of how to solve this problem
efficiently with a fast and slow pointer strategy.  

This strat was pointed out as a possibility when looking at the solution but it is not super efficient,

This solution was actually MUUUCHCHHCHCHC closer than I thought.  I should have stuck with it because I probably would
have gotten the right answer.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from math import ceil
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node_count, node = 0, head

        #Could do this entire part with a fast and slow pointer approach
        while node:
            node_count += 1
            node = node.next
        #Get the half for insertions
        list_split = node_count//2
        half_node = head
        for i in range(list_split):
            half_node = half_node.next

        #Reverse half list
        curr_node, prev_node = half_node, None
        while curr_node:
            tmp = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = tmp
        
        reversed_nodes, curr = curr_node, head
        while reversed_nodes and reversed_nodes:
            temp_cur, tmp_half = curr.next,reversed_nodes.next
            curr.next = reversed_nodes
            reversed_nodes.next = temp_cur
            reversed_nodes = tmp_half

        return 


        

