# 152_Maximum Product Subarray
# 见数组152
# 每个点有2个要记录的值: 含数i时的当前最小/最大 
# 每个点求值时有两种选择: 累成之前/重新开始 => min(num * small, num * large, num), max(num * small, num * large, num)
# 每个点仅由上一个点决定 => dp空间O(1)

class Solution:
  def maxProduct(self, nums):
    res = small = large = nums[0]
    for num in nums[1:]:
      small, large = min(num * small, num * large, num), max(num * small, num * large, num)
      res = max(res, large)
    return res