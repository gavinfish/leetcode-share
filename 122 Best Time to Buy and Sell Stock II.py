'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        low = high = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[i - 1]:
                high = prices[i]
            else:
                profit += high - low
                low = high = prices[i]
        profit += high - low
        return profit


if __name__ == "__main__":
    assert Solution().maxProfit([2, 4, 6, 1, 3, 8, 3]) == 11