'''
For this problem, there are a few things we need to realize in order to get to a working solution:

1) The real thing we are trying to find here is if the cars meet before or at the target.  We can do this by checking
   the time each car crosses the target.  If the one car behind another crosses the target faster, we know that they
   would have intersected at one point before they both hit the target
2) It does not matter where those cars intersect, only that the cas did at one point.

To do this, we can iterate over all cars in order of the cars that are closest to the target from furthest to the
target.  When doing that, we can check the cars arrival time with a stack containing the arrival time of the cars that
had arrived before.  We can check to see if the top arrival time on the stack is less than the current car's arrival
time.  If the current arrival time is smaller than the top of the stack, then that means that the current car gets to
the target quick and would have intersected with the car at the top of the stack before that point.  Therefore, we know
that those two cars are in the same fleet and the current car would have arrived at the same time as the top of the
stack.  At the end of iterating through all the cars, the length of the stack will represent the number of fleets.
'''

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p,s in zip(position,speed)]
        pairs.sort(reverse=True) # OR could use pairs.sort(reverse=True)

        arrival_stack = []
        for p,s in pairs:
            arrival = (target - p)/s
            if len(arrival_stack) >= 1 and arrival_stack[-1] >= arrival:
                continue
            arrival_stack.append(arrival)

        return len(arrival_stack)