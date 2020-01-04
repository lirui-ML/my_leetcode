# -*- coding: utf-8 -*-

"""
描述：买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

"""

class Solution:
    def maxProfit(self, prices) -> int:
        # 暴力解法 时间复杂度为 O(n^2)
        max_profit = 0
        days = len(prices)
        
        for i in range(days - 1):
            for j in range(i + 1, days):
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]
        return max_profit
    
    def maxProfit2(self, prices) -> int:
        # 时间复杂度 O(n)
        minprice = prices[0]
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice
        return maxprofit
        
if __name__=="__main__":
    prices = [7,1,5,3,6,4]
    s = Solution()
    res = s.maxProfit2(prices)
    
    