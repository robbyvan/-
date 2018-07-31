# 486_Predict the Winner
# DP, 两个人分别用 + 和 - 代替, 以A为视角, A +, B- 最后结果>0 => 赢
# 求(i, j), max(nums[i] - dp(i + 1, j), nums[j] - dp[i, j - 1])
# 或者递归top down.

class Solution:
  def PredictTheWinner(self, nums):
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
      dp[i][i] = nums[i]
      for j in range(i + 1, n):
        dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
    return dp[0][-1] >= 0

  # def PredictTheWinner(self, A):
  #   self.memo = {}
  #   self.nums = A
  #   return self.helper(0, len(self.nums) - 1) >= 0

  # def helper(self, left, right):
  #   if left > right:
  #     return 0
  #   if left == right:
  #     return self.nums[left]
  #   if not (left, right) in self.memo:
  #     l = - self.helper(left + 1, right) + self.nums[left]
  #     r = - self.helper(left, right - 1) + self.nums[right]
  #     self.memo[(left, right)] = max(l, r)
  #   return self.memo[(left, right)]