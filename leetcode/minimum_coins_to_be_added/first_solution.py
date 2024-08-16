'''
coins -> list of values of coins
target -> 

x is obtainable if a permutation of x that sums to x
given a subarray of coins from 1 to target, 

retun: int -> given a subarray of coins from 1 to target what is the min number of coins of any value that would make coins[1:target+1] a ,


target = 10
[5]
[1]
1+x = 2
2+x = 3
able: {5}
notAble: {1,2,3,4,6,7,8,9}
for 1: [1]
for 2: [1,1] || [2]
fpr 3: [1,1,1], [1,2], [3]
for 4: [1,1,1,1] || [1,1,2], [2,2], [1,3] [4] 
for 5: [1,1,1,1,1] || [1,2,2]
for 6: [1 2 3]
for 7: [1 2 4]
for 8: [1 2 4 8]

every even number from 1-target and + 1

[5]
0-4 3
6-10 3 [6,1,1,2]
any number + [1-4] it is at most 4 -> base + [1,1,2]


[4,5,6,7] target = 11
1 2 8 10

[1,1,1] target 5

[1,9,10,11] target 12

[5] target 10

[1,2,4] target = 8

1 loop through 1 - target
    1a. while currsum <= target at next item in coins to currSum
    1b. if currsum == tagrget-1 continue
    1c if currsum > target currsum-target//2
    1d if at end of list break out of loop and add (target - currsum)//2

x=1
idx=1
while n in 1-target
    if idx in range(len(coins)) and coins[idx]==n
        idx+=1
        continue
    else
        addCoinToCount
        n = (2*n+1)

'''

class Solution(object):
    def minimumAddedCoins(self, coins, target):
        coins.sort()
        extraCoinCount = 0

        oneCount = 0
        idx=0
        while idx < len(coins) and coins[idx]==1:
            oneCount+=1
            idx+=1
        if oneCount==0:
            extraCoinCount+=1

        n=((2*(oneCount))+1)
        while n in range(0,target+1):
            while idx in range(len(coins)) and coins[idx]<n:
                idx+=1
            
            if idx == len(coins):
                return extraCoinCount
                
            print(n+1, idx,coins[idx])
            if coins[idx]==n+1 or coins[idx]+1==n+1:
                n=((2*(n))+1)
            else:
                print("here")
                extraCoinCount+=1
                n = ((2*(n))+1)
        return extraCoinCount


        