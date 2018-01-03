# 62_Unique Paths
# dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
# 初始化第一行列为1

class Solution:
  def uniquePaths(self, m, n):
    if m == 0 or n == 0:
      return 0
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
      dp[i][0] = 1
    for j in range(n):
      dp[0][j] = 1

    for i in range(1, m):
      for j in range(1, n):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]
