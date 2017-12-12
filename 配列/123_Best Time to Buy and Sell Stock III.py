# 123. Best Time to Buy and Sell Stock III
# 方法1:
# 遍历两次, 从前往后&从后往前 [0, i] + [i, -1]找到最大
# 从前往后:
#     保持更新最小, 段利润为(当前 - 最小), 存入DP表
# 从后往前:
#     保持更新最大, 段利润为 (最大 - 当前), 和DP表相加更新总利润.

class Solution:
  def maxProfit(self, prices):
    if len(prices) == 0:
      return 0
    profits = []
    low = prices[0]
    profit = 0
    for i in range(len(prices)):
      low = min(low, prices[i])
      profit = max(profit, prices[i] - low)
      profits.append(profit)

    high = prices[-1]
    profit = 0
    maxEarn = 0
    for i in range(len(prices) - 1, -1, -1):
      high = max(prices[i], high)
      profit = high - prices[i]
      maxEarn = max(profit + profits[i], maxEarn)
    return maxEarn