'''
This is a classic sliding window problem where we are asked to find the max profit we can make given a list numbers that
represent the stocks value on a day by day basis.  We can buy the stock on one day and then sell the stock on another.
NOTE* This problem states that we can only buy on a signle day and sell on a single day so we cannot make multiple
purchases or sell on multiple days.

To solve this problem, first we must recognize that what we are look for is the max profit which is represented with the
formula profit=price[i+1]-price[i].  It is also important to notice that we can only move through the array from
left to right because we cannot go back in time.  Further, we can make the statement that if price[i] < price[i+1], then
we know that we should set the base price at i+1 because any day that reaps profit in the future will have more earnings
if we use the day where prices are least to buy the stock.  With all of that said, we can use a sliding window strategy
where we set a left and right pointer at the starting two indexies in the list.  If the value at the right index is greater
than the value at the left, we can move the left over to create a wider window looking for a larger number.  Further,
each time we move the right pointer over, we save the max_profit because there could be spikes and drops that are made
of numbers greater than our left most value so we want to keep track of the max.  If we hit a value with the right
ponter that is less than the left, we want to reset our base because at that point we know that any value after the left
will make more money using that base so we shift our left and right pointers to those values.
'''

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        l,r = 0, 1
        profit = 0
        while r <= len(prices)-1:
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                profit = max(profit, prices[r]-prices[l])
                r += 1

        return profit