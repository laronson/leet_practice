'''
This problem presents another sorted array that has been rotated to the right x number of times (e.g. [1,2,3] ->
[3,1,2]), and we are tasked with finding an integer target in the array.  This, like the other sorted and rotated array
can use the binary search strategy to find the target within this array.  Although the numbers are not sorted in a
strict top to bottom fasion, the number are still sorted and we can use this during our searching logic.  If the number
at hte middle of the array is greater than the target AND the value at the right pointer is greater than the middle
value, then we know that the value must be in the right side of the array so we can shift our pointer accordingly.  Same
goes for the other four cases in the searching logic where we use the target, mid, r and l pointers to determine the
direction of our search.
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<=r:
            mid = (r+l)//2

            if target == nums[mid]:
                return mid
            elif nums[mid] > target:
                if nums[mid] > nums[r]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                if nums[mid] > nums[r]:
                    r = mid-1
                else:
                    l = mid+1
        
        return -1