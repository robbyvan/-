# 122_Best Time to Buy and Sell Stock II
# 参见"数组"122, 注意循环到最后一项时, 有可能还是更新了high, 因此要手动加上最后的high - low

class Solution:
  def maxProfit(self, prices):
    if len(prices) < 2:
      return 0
    low = high = prices[0]
    profit = 0

    for day in range(1, len(prices)):
      if prices[day] > high:
        high = prices[day]
      else:
        profit += (high - low)
        low = high = prices[day]
    profit += (high - low)
    return profit