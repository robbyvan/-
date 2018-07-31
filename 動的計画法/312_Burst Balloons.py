# 312_Burst Balloons
# 考虑问题(i, j)中, 最后扎破k: 
# (i, j) = max{ (i, k) + (k, j) + nums[i - 1] * nums[k] * nums[j + 1] }
# 递归(i, j), 基础情况: 1)如果已经计算了(i, j)或者i, j相邻: 返回dp[i][j]
# 迭代(i, j): 从gap = 2开始直到gap = n - 1 => for gap in range(2, n)
# 再考虑开头i从0 -> n - gap
# dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]) 代表i, j之间, 不含i, j全部扎破

class Solution:
  def maxCoins(self, nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    def calculate(i, j):
      if dp[i][j] or i + 1 == j:
        return dp[i][j]
      coins = 0
      for k in range(i + 1, j):
        dp[i][j] = max(coins, calculate(i, k) + calculate(k, j) + nums[i] * nums[k] * nums[j])
      dp[i][j] = coins
      return coins

    return calculate(0, n - 1)


class Solution:
  def maxCoins(self, nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    for gap in range(2, n):
      for l in range(0, n - gap):
        r = l + gap
        for k in range(l + 1, r):
          dp[l][r] = max(dp[l][r], dp[l][k] + dp[k][r] + nums[l] * nums[k] * nums[r])

    return dp[0][-1]

