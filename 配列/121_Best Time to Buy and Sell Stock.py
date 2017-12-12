# 121. Best Time to Buy and Sell Stock
# 遍历一次, 假设从[0]买入, 开始遍历:
# 如果更低价, 修改买入 (因为之后高价的产生的利润一定比之前的多, 要么更多, 要么时间逆序了没有)
# 否则计算利润, 如果利润更大就更新利润

class Solution:
  def maxProfit(self, prices):
    if len(prices) == 0:
      return 0
    buy, sell, profit = prices[0], 0, 0
    for i in range(1, len(prices)):
      if prices[i] < buy:
        buy = prices[i]
      else:
        if prices[i] - buy > profit:
          profit = prices[i] - buy
    return profit