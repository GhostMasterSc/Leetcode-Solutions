class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_seen = prices[0]
        profit = 0

        for i in range(1,len(prices)):
            if prices[i]<min_seen:
                min_seen = prices[i]
            elif prices[i] - min_seen > profit:
                profit = prices[i] - min_seen

        return  profit
