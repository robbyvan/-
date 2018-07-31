# 322_Coin Change
# dp[0] = 0, 初始化为max(含有意义)
# 对于所有amount, 循环coins里的coin, dp[i] = min(dp[i - c]) + 1

class Solution:
  def coinChange(self, coins, amount):
    MAX = float("inf")
    dp = [0] + [MAX] * amount

    for i in range(1, amount + 1):
      dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

    return -1 if dp[amount] == MAX else dp[amount]

# class Solution:
#   def coinChange(self, coins, amount):
    # if amount < 0:
    #   return -1
    # if amount == 0:
    #   return 0

    # dp = [0]
    # for money in range(1, amount + 1):
    #   dp.append(-1)
    # for coin in coins:
    #   if coin <= amount:
    #     dp[coin] = 1

    # for target in range(1, amount + 1):
    #   opt = float("inf")
    #   for coin in coins:
    #     need = target - coin
    #     if need >= 0:
    #       if dp[need] != -1:
    #         opt = min(opt, dp[need] + 1)
    #   if opt == float("inf"):
    #     dp[target] = -1
    #   else:
    #     dp[target] = opt

    # return dp[amount]
