'''
WORKS!!

'''

class Solution(object):
    def minimumAddedCoins(self, coins, target):
        coins.sort()
        extraCoins = 0
        targetPlace = 1
        idx = 0

        while idx < len(coins) and coins[idx]==1:
            targetPlace+=1
            idx+=1

        cIdx=idx
        while cIdx in range(idx,len(coins)):
            print("start",coins[cIdx],targetPlace)
            if targetPlace > target:
                break
            
            while coins[cIdx] > targetPlace:
                print("awefa",coins[cIdx],targetPlace)
                extraCoins+=1
                targetPlace = (2*(targetPlace-1)+2)

            targetPlace += coins[cIdx]
            cIdx+=1

        print(targetPlace, target)

        while targetPlace <= target:
                extraCoins+=1
                targetPlace = (2*(targetPlace-1)+2)
        
        print(targetPlace, target)
        return extraCoins 




        