# 63_Unique Paths II
# dp.
# 初始化的时候第一行列遇到0, 则其之后都是0(不是1)
# 递推公式(一个加法)只在该点不是障碍的时候成立.否则是0


class Solution:
  def uniquePathsWithObstacles(self, obstacleGrid):
    m = len(obstacleGrid)
    if m == 0:
      return 0
    n = len(obstacleGrid[0])
    if n == 0:
      return 0

    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
      if obstacleGrid[i][0] == 0:
        dp[i][0] = 1
      else:
        break
    for j in range(n):
      if obstacleGrid[0][j] == 0:
        dp[0][j] = 1
      else:
        break

    for i in range(1, m):
      for j in range(1, n):
        if obstacleGrid[i][j] == 1:
          dp[i][j] = 0
        else:
          dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]