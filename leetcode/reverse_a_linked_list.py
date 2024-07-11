'''
This standard linked list problem presents us with a singly linked list and asks us to reverse the nodes within that 
list.  This problem forces you to think a bit differently about how to manipulate linked lists.  In most cases, you may 
think of linked list manipulation in terms of moving nodes to a different place within the list.  However, in the case 
of reversing a linked list, it becomes important to think about the direction of the links rather than the placement of 
the nodes.

To reverse the linked list, you want to flip the direction of the node links and keep the nodes in place.  As a visual 
example, this would look something like this: 
1 → 2 → 3 ————> 1 ← 2 ← 3
In this case, 3 would end up being the head of the reversed linked list. 

In order to do this, we must iterate through the list using a prev and curr pointer which points to two nodes next to 
each other in the list.  Each iteration, can take the node.next of curr and point it to prev while keeping track of 
where the next iteration’s prev and curr pointers should go.  At the end of our iteration which breaks when curr == None
(aka we set curr equal to the end of the original list) we can return the prev pointer as the head of the reversed list.  
It is the case that we return prev because curr will have iterated off the end of the list while prev points to the end.
'''

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr = None, head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev