# Brute force Solution
# Time: O(2^n), Space: O(n)
# Where n is the number of items.
class RecursiveSolution:
    def dfs(self, profit, weight, capacity):
        return self.dfsHelper(0, profit, weight, capacity)

    def dfsHelper(self, i, profit, weight, capacity):
        if i == len(profit):
            return 0

        # Skip item i
        maxProfit = self.dfsHelper(i + 1, profit, weight, capacity)

        newCap = capacity - weight[i]
        if newCap >= 0:
            p = profit[i] + self.dfsHelper(i + 1, profit, weight, newCap)
            # Compute the max
            maxProfit = max(maxProfit, p)
        
        return maxProfit


profit = [4,4,7,1]
weight = [5,2,3,1]
capacity=8
rs = RecursiveSolution()

x = rs.dfs(profit,weight,capacity)
print(x)