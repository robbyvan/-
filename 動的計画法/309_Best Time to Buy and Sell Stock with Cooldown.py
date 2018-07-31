# 309_Best Time to Buy and Sell Stock with Cooldown
# 三种状态, buy, rest, sell.
# 代表在day之前所有的以buy, rest, sell结束的序列的最大profit

class Solution:
  def maxProfit(self, prices):
    if len(prices) < 2:
      return 0
    buy, sell, rest = -prices[0], 0, 0
    for i in range(1, len(prices)):
      prevBuy, prevSell = buy, sell
      buy = max(buy, rest - prices[i])
      sell = max(sell, buy + prices[i])
      rest = max(rest, prevSell, prevBuy)
    return max(rest, sell)