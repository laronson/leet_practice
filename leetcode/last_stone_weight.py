'''
4,3,2,1 -> 2,1,1 -> 1,1 -> []
5,3,2,1 -> 2,2,1 -> 1

heap,

1. create max heap from stones
2. loop while length of stoneHeap is > 1
3. take top two stones off of heap and perform simulation
4. if stone remaining after simulation, push back onto heap
5. return last remaining stone on heap or 0 

5,3,2,1
maxHeap: 5, 3, 2, 1 -> 2,2,1 -> 1
'''

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
      #invert to create maxHeap representation
      maxHeap = [stone*-1 for stone in stones]
      heapq.heapify(maxHeap)

      while len(maxHeap) > 1:
        #re-invert values after pulling off of maxHeap representation
        s1, s2 = heapq.heappop(maxHeap)*-1, heapq.heappop(maxHeap)*-1

        if s1 > s2:
          heapq.heappush(maxHeap,-1*(s1-s2))
        elif s2 > s1:
          heapq.heappush(maxHeap,-1*(s2-s1))
      
      # Remember to re-invert value from maxHeap before returning it
      return 0 if not maxHeap else maxHeap[0]*-1 