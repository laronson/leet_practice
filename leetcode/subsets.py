'''
This problem presents us with a list of numbers and asks us to generate all of the subsets that can be created using the 
numbers within the list where duplicates are not allowed.

To solve this problem, we first must think about how we construct a subset.  When looking at each individual number in 
the list, we have a choice (yes/no) to add that number to the subset.  Using this logic, building a subset is a chain of 
these yes/no decisions where for each number in the list, we decide if the number will be in the subset or not.  
Therefore, each subset in the list of all subsets is a different combination of yes or no decisions on where or not a 
number is or is not in the subset making the total number of subsets 2^n where n is the number of numbers in the numbers 
list.

To code a solution to generate each subset, we can use a recursive dfs search where, for each number in the list of 
numbers, we branch for the condition of adding the number to a subset and branch another time for the condition of not 
adding the number to the subset.  As we recursively trace through the numbers array using this conditions, we keep track 
of what the subset would look like at each branch.  Once we hit the end of the numbers array for each decision chain, 
we save the subset in a results array.  For example, for the array [1,2,3] some decision chains would look like:
- yes 1, no 2, no 3 → [1]
- yes 1, yes 2, no 3 → [1,2]
- no 1, yes 2, yes 3 → [2,3]

Once the dfs traversal has completed, we return the results array containing all sub arrays.
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subList=[]
        subset = []

        def dfs(idx):
          if idx >= len(nums):
            subList.append(subset.copy())
            return
          
          subset.append(nums[idx])
          dfs(idx+1)
          subset.pop()
          dfs(idx + 1)
        
        dfs(0)
        return subList