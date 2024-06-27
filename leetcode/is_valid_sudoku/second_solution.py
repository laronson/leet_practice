'''
This is a bit better than the first solution because we are not using as many loops to generate the squares as we were
in the first solution.  That saves us a bunch of time as we only need to iterate through the board once as we generate
the squares.

The other main difference is that, using this checking strategy we need to store our checking sets in the top level 
function.  This causes a bit of a downfall in memory performance but because of the huge gain in speed it seems worth it
'''

from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        #keyed by a tuple of (row//3,col//3) using the floor-divide operator which will get us a different tuple for every combination or row/col
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                current_space = board[row][col]
                if(current_space == '.'):
                    continue
                
                if (current_space in rows[row] or 
                    current_space in cols[col] or
                    current_space in squares[(row//3,col//3)]
                    ): 
                    return False

                rows[row].add(current_space)
                cols[col].add(current_space)
                squares[(row//3,col//3)].add(current_space)
        return True

                

                