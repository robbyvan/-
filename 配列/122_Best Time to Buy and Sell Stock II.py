# 122. Best Time to Buy and Sell Stock II
# 遍历一次, 还是从[0]买入, 开始遍历
# 如果遇到比peak大的价格, 持续更新peak.
# 否则:
# 当前peak - valley计算前一段的最大利润, 然后更新下一段的low, high为当前i值
# *最后一次跳出循环需要再加上最后一段的利润.

class Solution:
  def maxProfit(self, prices):
    if len(prices) == 0:
      return 0
    low, high, profit = prices[0], prices[0], 0
    for i in range(1, len(prices)):
      if prices[i] > high:
        high = prices[i]
      else:
        profit = profit + high - low
        low = high = prices[i]
    profit = profit + high - low
    return profit