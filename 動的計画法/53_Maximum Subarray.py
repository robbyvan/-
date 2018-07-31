# 53_Maximum Subarray
# 每个点有一个值: 最大值 = max(num, val + num) => 两种选择: 累加之前/重新开始
# 类似max product, 有两个状态, max和min

class Solution:
  def maxSubArray(self, nums):
    if not nums:
      return 0
    res = val = nums[0]
    for num in nums[1:]:
      val = max(num, val + num)
      res = max(res, val)
    return res
