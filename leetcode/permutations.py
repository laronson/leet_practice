class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
      numSet, res = set(nums), []

      def generatePermutations(perm, numSet):
        if not numSet:
          res.append(perm.copy())
          return
        
        # Could possibly remove the .copy here
        for n in numSet.copy():
          perm.append(n)
          numSet.remove(n)
          generatePermutations(perm,numSet)
          perm.pop()
          numSet.add(n)

      generatePermutations([], set(nums))
      return res

        