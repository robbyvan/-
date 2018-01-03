# 64. Minimum Path Sum
# DP, 需要初始化row = 0和col = 0的格子.
# 空间复杂度O(m+n)或者O(n)或者直接在grid修改
class Solution:
  def minPathSum(self, grid):
    m, n  = len(grid), len(grid[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1, m):
      dp[i][0] = dp[i - 1][0] + grid[i][0]
    for j in range(1, n):
      dp[0][j] = dp[0][j - 1] + grid[0][j]
    for i in range(1, m):
      for j in range(1, n):
        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    return dp[-1][-1]
