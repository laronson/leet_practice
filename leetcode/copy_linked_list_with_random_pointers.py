'''
This solution presents us with a Linked List and we are asked to deep copy the linked list  and return that copy.  The 
twist here is that the linked list we are given has a typical node.next pointer but it also has a node.random pointer 
that points to a random node within the linked list.  Our copy needs to contain the pointers to the new nodes at .next 
and to .random for each node.

In order to do this, we need to use a two-pass strategy and and a hash map.  On the first pass through the linked list, 
we need to create new nodes for each node in the original list and use them as the values of a dictionary that is keyed
 using the nodes from the original list.  The code to put these nodes into our dictionary would look something like 
 this: 
 node_map[original_node] = copied_node.  
 
 Once we have that linkage, we can loop through the original node again 
 and use the node from the original node to key the nodes for the pointers at the corresponding node in the new list.  
 For example, the code to set a new node.next in the list would look something like this: 
 new_node.next = node_map[original_node.next].  
 
 Using this strategy, we iterate through every node in the original node to generate the new list.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        node = head
        node_map = {}

        while node:
            copy = Node(node.val)
            node_map[node] = copy
            node = node.next
        
        node = head
        dummy_copy = copy_head = Node(0, None, None)
        while node:
            dummy_copy.next = node_map[node]
            dummy_copy.next.next = node_map[node.next] if node.next in node_map else None
            dummy_copy.next.random = node_map[node.random] if node.random in node_map else None

            dummy_copy = dummy_copy.next
            node = node.next
        
        return copy_head.next


        

        