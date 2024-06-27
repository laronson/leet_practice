'''
This solution works, but it is probably inefficient.  The program is passable and does seem to beat most on memory but
it still has a memory footprint of O(n**2) so I wouldn't call it a significant win.  The main strategy behind this 
solution is to use generators to create the sub-sets of the board that we need to inspect.  When inspecting, we can
use a set and store the valid numbers in that set to see if we end up adding any duplicates as we iterate through the
board grouping.

This is probably a bit more efficient on memory due to garbage collection every.  Because we run our checks in a sub
function instead of storing our sets we use to check in the top level function, the sets are most likely garbage
collected when we exit the check function.  Its not better in theory but because of garbage collection we may be getting 
an extra boost in this case.
'''

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.isValidGroup(row):
                return False

        for i in range(9):
            col = [board[row][i] for row in range(9)]
            if not self.isValidGroup(col):
                return False
        
        for i in range(0,8,3):
            three_rows = board[i:i+3]
            for sec_start in range(0,8,3):
                section = sum([three_rows[row][sec_start:sec_start+3] for row in range(3)], []) 
                if not self.isValidGroup(section):
                    return False

        return True

    def isValidGroup(self, group: List[str])->bool:
        group_set=set()
        for s in group:
            if s != '.' and s in group_set:
                return False
            group_set.add(s)
        return True
        