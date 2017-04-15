'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total_max_profit = 0
        n = len(prices)
        first_profits = [0] * n
        min_price = float('inf')

        for i in range(n):
            min_price = min(min_price, prices[i])
            total_max_profit = max(total_max_profit, prices[i] - min_price)
            first_profits[i] = total_max_profit

        max_profit = 0
        max_price = float('-inf')
        for i in range(n - 1, 0, -1):
            max_price = max(max_price, prices[i])
            max_profit = max(max_profit, max_price - prices[i])
            total_max_profit = max(total_max_profit, max_profit + first_profits[i - 1])
        return total_max_profit


if __name__ == "__main__":
    assert Solution().maxProfit([2, 4, 6, 1, 3, 8, 3]) == 11
    assert Solution().maxProfit([1, 2]) == 1