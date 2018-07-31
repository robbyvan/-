# 303_Range Sum Query - Immutable
# 求sum(i, j), sum(j) - sum(i - 1)

class NumArray(object):
  def __init__(self, nums):
    self.arr = list(nums)
    if len(nums) > 0:
      self.dp = [0] * len(self.arr)
      self.dp[0] = self.arr[0]
      for i in range(1, len(self.arr)):
        self.dp[i] = self.arr[i] + self.dp[i - 1]

  def sumRange(self, i, j):
    if i < 0 or i > len(self.arr) - 1 or j < 0 or j > len(self.arr):
      return False
    if i == 0:
      return self.dp[j]
    return self.dp[j] - self.dp[i - 1]