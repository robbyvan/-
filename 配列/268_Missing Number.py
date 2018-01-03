# 268_Missing Number
# 求和公式相减; 异或; 排序 + 二分查找

class Solution:
  def missingNumber(self, nums):
    res = len(nums)
    for i in range(len(nums)):
      res ^= i
      res ^= nums[i]
    return res