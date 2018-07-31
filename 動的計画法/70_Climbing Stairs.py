# 70_Climbing Stairs
# dp.append(dp[stair - 1] + dp[stair - 2])

class Solution:
  def climbStairs(self, n):
    if n == 1:
      return 1
    dp = [1, 2]
    for stair in range(2, n):
      dp.append(dp[stair - 1] + dp[stair - 2])
    return dp[-1]
