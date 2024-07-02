'''
This problem presents a list of integers where the values in the list range from [1-n] and there are n+1 integers in the
list.  This problem is a trick problem and you need to understand how to solve the problem below using the following two
strategies: 

linked list cycle - This problem can be considered a linked list problem where the indecies of the array are the 
nodes in the linked list, and the values at those indecies are the pointers to whichever node conmes next in the list.  For
example, the list [1,2,0] would be a cycled linked list that looks like node0(1) -> node1(2) -> node2(0) -> node0(1)....  Because
we know that the list in the problem contains numbers in range of [1-n] and the list only contains n+1 entries, we know that each
value in the list will point to a valid node number within our theoretical linked list.  We also know that the list will contain a
cycle because numbers in the list are repeated which means that nodes will be revisited  Using floyds algorithm (listed below), we
can find a cycle in list and the node that is at the start of the cycle will be the repeated number.

Floyds Algorithm - Like the veratasium prison problem where the prisoners have to pick the briefcase with a specific number
in it and the solution is to pick a box and then go to that box numbered with the number inside of the box.  Floyds algo 
states that in a linked list that contains a cycle, the start of the list is always going to be the same number of nodes 
away from the point where a fast and slow pointer first intersect.  Therefore, in our solution, we can find the point at which
a fast and slow pointer intersect.  Then, we can put a pointer at the start and then at the intersection we found, iterate those 
pointers through the list starting at those respective points.  Because the intersection and the start of the list will be the same
number of points away from the start of the cycle (aka the duplicated value), we know that the fast and slow pointers will eventually
meet at that point which will get us our answer 
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0,0

        #Find the intersection of the loop that is created by the numbers and their indexes
        #When fast and slow are equal, it does not mean that there are two different values in the list that are
        #equal but that at point slow, fast also visits there, and this is the first occurance of that happening 
        while True:
            slow = nums[slow] #iterate to the next node in the list at the value stored at nums[slow]
            #This iterates through the list at double speed because if num[x] represents the link to the next node 
            #in the list (aka node.next) nums[nums[x]] will represent the node two points away (aka node.next.next)
            fast = nums[nums[fast]]
            print(slow,fast)
            if slow == fast:
                break

        #Iterate the pointer at the intersection of fast and slow at the slow pointer and then create a new pointer
        #slow2 to iterate from the start of the array
        slow2 = 0 #Pointer at start of the array
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        

        