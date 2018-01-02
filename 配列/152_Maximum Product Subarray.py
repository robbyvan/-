# 152. Maximum Product Subarray
# dp 选择存储max min 自身


class Solution:
  def maxProduct(self, nums):
    maxim = big = small = nums[0]
    for n in nums[1:]:
      big, small = max(n, n*big, n*small), min(n, n*big, n*small)
      maxim = max(maxim, big)
    return maxim
