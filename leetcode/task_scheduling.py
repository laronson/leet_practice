'''
1. group tasks and count -> python Counter -> MaxHeap
2. execute tasks by count # -> loop through task maxHeap and execute top task
3. When task is executed, wait n seconds before executing task of same type -> pull max off heap and throw onto queue 
with time 
4. in meantime, execute tasks of other types repeating steps 2-3 -> pull off max heap
5. When task list is empty, we are done -> When task heap and queue are empty we are done

X Y X X n=2

heap 3X 1Y -> 1Y -> [] -> [] ->  [] -> []
queue [] -> 2X|1 -> 2x|1  -> 1x|3  > 1x|3 -> []
time 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
'''

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
      tcount = Counter(tasks)
      maxHeap, q, time = [c*-1 for c in tcount.values()], deque(), 0
      heapq.heapify(maxHeap)

      # 3X 1Y
      while maxHeap or q:
        time+=1
        if q and q[0][1] < time - n:
          taskcount,_ = q.popleft()
          heapq.heappush(maxHeap, taskcount)
        
        if maxHeap:
          taskcount = heapq.heappop(maxHeap)
          if taskcount + 1 < 0:
            q.append((taskcount+1,time))

      return time