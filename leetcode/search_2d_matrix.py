'''
This problem resents a 2d matrix of numbers that are sorted in accending order from top left to bottom right (aka
matrix[0][n] will always be greater than matrix[1][n]).  We are tasked with determining if a target number exists inside
of the 2d matrix.  To do this, we can use binary search in two different places.  First, we can use binary search to
determine which row to look in.  Once we find the row that contains the target, we use binary search again to find if
the target exists in the row.
'''

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def does_exist(row:List[int])->bool:
            l,r = 0,len(row)-1

            while l <= r:
                mid = l + (r-l)//2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    l = mid+1
                else: 
                    r = mid-1
            
            return False

        top, bottom = 0, len(matrix)-1
        while top<=bottom:
            mid = top + (bottom-top)//2
            if matrix[mid][0] <= target and matrix[mid][len(matrix[0])-1] >= target:
                return does_exist(matrix[mid])
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                top = mid + 1

        return False
