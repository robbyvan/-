# 238_Product of Array Except Self
# 2 passes
# 从左->右, 从右->左 各一次
class Solution:
  def productExceptSelf(self, nums):
    n = len(nums)
    res = [1] * n
    for i in range(1, n):
      res[i] = res[i - 1] * nums[i - 1]
    m = 1
    for i in range(n - 1, -1, -1):
      res[i] = res[i] * m
      m *= nums[i]
    return res

