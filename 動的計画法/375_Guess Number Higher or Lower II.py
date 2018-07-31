# 375_Guess Number Higher or Lower II
# 初始化dp补1行: 为了使得对应上1~n.
# dp, (i, j) = min(k + (i, k - 1), (k + 1, j) for k in (i => j))
# 注意for i in range(n, 0, -1): for j in range(i + 1, n + 1):才是从小 => 大的循环顺序

class Solution:
  def getMoneyAmount(self, n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n, 0, -1):
      for j in range(i + 1, n + 1):
        dp[i][j] = min(k + max(dp[i][k - 1], dp[k + 1][j]) for k in range(i, j))
    return dp[1][n]