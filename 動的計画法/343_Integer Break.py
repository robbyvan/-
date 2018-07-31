# 343_Integer Break
# bottom-up: 从小到大, 保证划分成两份, 结果取最大乘积
# max(直接两个数相乘, 一个数*另一个数的划分, 两个数的划分)

class Solution:
  def integerBreak(self, n):
    dp = [1] * (n + 1)
    for i in range(2, n + 1):
      temp = 1
      for k in range(1, i):
        temp = max(temp, dp[k] * dp[i - k], k * dp[i - k], dp[k] * (i - k), k * (i - k))
      dp[i] = temp
    return dp[-1]