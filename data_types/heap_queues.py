'''
Heap Queues are lists that maintain an order of the heap's elements. In python, heaps are not really their own
data structure but are Lists that are maintained as heaps using phythons Heap Queue Algorithm.

In a heap the smallest element in the heap is always at the root of the heap (heap[0]) and the largest element 
in the heap is at the top of the heap (heap[len(heap)]).  

Heaps are created by either instantiating a new List using [] or by using the heapify() function that creates the heap 
from an existing list in place in linear time.
'''

# Create an empty heap
from heapq import heapify


emptyHeap = []
#create a heap from an existing list
existingList = [3,2,1]
newHeap = heapify(existingList)
