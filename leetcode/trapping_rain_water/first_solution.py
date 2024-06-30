'''
water at x between two heights:
h_curr - min(h1,h2)

This solution works for most cases but fails when in the case where, when searching the end of the array, your right
pointer hits the end of the array before it hits a value that is greater than or equal to the value at left.  An example
of this would be [...,3,2,1,2].  If your left ends up at 3, your right pointer will iterate to the end of the array and
only hit 2s and 1s which never triggers the code to add the water that can fit in the [2,1,2] segment.  Therefore, we
need another strategy to account for searching at the end of the array.  ** Look at second solution
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0

        l,r = 0, 1
        max_water = 0

        while r < len(height):
            if height[l] > height[r]:
                r += 1
                continue
            
            for i in range(l+1,r):
                if l == 0 and height[r] > height [l]:
                    break
                if r == 0 and height[l] > height[r]:
                    break

                max_water += min(height[l],height[r]) - height[i]
            
            l = r
            r += 1
            
        return max_water

            

                

