'''
For this solution, we start with pointers at the left and right of the heights list.  As we increase our left pointer to
the right, we check to see what the max amount of water we can store to the left is (based off of the values to the
right of it) and same as we increase our right pointer to the left.  We then add that max amount of water to a max
total.  The reason this works is because, as we move left to right, we set the max to be the highest value we have seen
which means that, ever water value we calculate will only be based off of the max value we have seen so far, getting us
the most possible water we can hold at any given space.  Same goes for the right side of the list as we increase.  

Further, we only increase right or left depeneding on which one has the higher max value at the time of iteration.
Therefore, we are garunteed that left and right will meet at the highest point(s) in the list, ensuring that we do not
double count water values.
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0

        l,r = 0, len(height)-1
        max_left, max_right = height[l], height[r]
        max_water = 0

        while l<r:
            if max_left < max_right:
                l += 1
                max_left = max(max_left, height[l])
                max_water += max_left - height[l]
            else:
                r -= 1
                max_right = max(max_right, height[r])
                max_water += max_right - height[r]

        return max_water