'''
coins - the values associated with the coins we have access to
amount - an integer that we must sum to using the values of the coins we have access to denoted by
  the values in the coins list
return: int - The minimum number of coins from the coins list that we need to use to sum to amount

amount=10 coins[1,2,5] return: 2 -> 5*2
amount=11 coins[1,2,5] return: 3 -> 5*2+1*1
amount=12 coins[1,2,5] return: 3 -> 5*2+2*1
amount=12 coins[2,5] return: -1 -> no possible way to ad to 12 with 2 and 5
amount=12 coins[13] return: -1 -> no possible way to ad to 12 with 13

amount = 

amount=11 coins[1,2,5]
11-5=6
6-5=1
1-1=0
3

amount 34 coins [3 4 11] 23 12 

1) sort list of coins o(coinslog(coins))
2) init coinIdx = len(coins)-1, amountPlaceholder=amount, subCount =0
3) iterate while coinIdx >=0 o(coins)
    while currCoin < amount o(amount)
      subtract currCoin from amount
      increase subCount
    coinIdx-=1
4) if there is still amount, return -1 otherwise return subCount


'''

'''
coins=[1,2,5]
amount=4
dp[1] = 1
dp[2]= 1
dp[3]=2
dp[4] = 12

'''

'''
This problem presents us with a list of coins where coins[i] represents the value of one of the coins in our set.  The 
problem also presents us with an amount and asks us to return the minimum number of coins from our list of coins we can 
use to sum to amount.

At first, I thought this problem could be solved using a greedy approach where I would first sort the values in coins.  
I could then loop through coins and always subtract the largest coin value from my amount remainder until I tried to 
subtract every coin value from amount.  I did this until I could not use any coin value to subtract from amount and 
reach 0 OR the amount had reached zero.  This would work for some cases but in others, the pathway this strategy led to 
would not give us the minimum amount of coins but may just give us some combination of coins that would add to amount.

To solve this problem, we needed to realize that this problem was actually a dynamic programming problem and that we 
could use a bottom-up approach to accurately solve this problem.  To do this, we could see how we could use our coins 
to make smaller amounts from 1-amount and then use those coin counts to see if we could get to our amount from 1 coin 
away from any other generated coin count amount.  For example, if we have the coins [1,2] and we are trying to get to 2, 
we can see that we can get to an amount 1 with 1 count.  Therefore, if we use a 1 coin to try to get to two, 2-1 = 1 so 
if we have calculated how many coins we use to take to get to 1, we can use that and add 1 to that count to get to two.  
However, in this case, we have a count that adds to 2.  Therefore, since it takes 0 coins to get to 0, and 2-2 = 0, then 
it takes the amount of coins it takes to get to 0 PLUS 1 coin to get to two (aka the 2 value coin).
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
      dp = [amount+1]*(amount+1)
      dp[0]=0

      for a in range(amount+1):
        for c in coins:
          if (a-c) >= 0:
            dp[a] = min(dp[a],dp[a-c]+1)
      
      return dp[amount] if dp[amount] != amount+1 else -1

        