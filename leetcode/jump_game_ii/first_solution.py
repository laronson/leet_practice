'''
** Works but needs refactoring **

[3,10,1,4,1,1,1]
 0 1  2 3 4 5 6

loop through jumps
  while looping through current space jump count, check for spot with max potentiential

  increase jmp count
  set start location to max potential spot and start again from there

max spaces needed to jump = len(nums)-1 - curr
if nums[curr] < maxSpacesNeeded
  numSpacesNeededSoFar - nums[cur]

'''

class Solution:
    def jump(self, nums: List[int]) -> int:
      if len(nums)==1:
        return 0
      if nums[0]>=len(nums)-1:
        return 1

      jumpCount = 0
      idx = 0

      while idx<len(nums)-1:
        jumpCount+=1

        currJumpCount = nums[idx]
        bestJumpPotential = 0
        nextJump = idx + currJumpCount

        while idx+currJumpCount in range(len(nums)) and currJumpCount > 0:
          potential = idx + currJumpCount + nums[idx + currJumpCount]
          if potential > bestJumpPotential:
            bestJumpPotential = potential
            nextJump = idx + currJumpCount
          currJumpCount-=1
        idx=nextJump

      return jumpCount
