# 96_Unique Binary Search Trees
# DP: dp[n]? 除去根, dp[左] * dp[右], 左: 0 -> n - 1

class Solution:
  def numTrees(self, n):
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    dp[1] = 1
    if n < 2:
      return dp[n]
    for i in range(2, n + 1):
      for left in range(i):
        dp[i] += dp[left] * dp[i - left - 1]
    return dp[n]
