# 121. Best Time to Buy and Sell Stock
# 遍历一次, 假设从[0]买入, 开始遍历:
# 如果更低价, 修改买入 (因为之后高价的产生的利润一定比之前的多, 要么更多, 要么时间逆序了没有)
# 否则计算利润, 如果利润更大就更新利润

class Solution:
  def maxProfit(self, prices):
    if len(prices) < 2:
      return 0
    profit, buy = 0, prices[0]
    for day in range(1, len(prices)):
      if prices[day] < buy:
        buy = prices[day]
      else:
        profit = max(profit, prices[day] - buy)
    return profit