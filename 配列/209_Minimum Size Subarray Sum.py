# 209. Minimum Size Subarray Sum
# 使用双指针, 指向段的左和右
# 每次加入一个新右, 看是否大于了target:s, 如果没有, 继续
# 否则大于s时, 说明是一个解, 记录res并更新min res, 然后扔掉左,并左 + 1
# 重复上面的过程, 直到右扫到nums最后一个数字

class Solution:
  def minSubArrayLen(self, s, nums):
    if not nums:
      return 0
    left, right, sums, res = 0, 0, 0, float('inf')
    while right < len(nums):
      sums += nums[right]
      while sums >= s:
        res = min(res, right - left + 1)
        sums -= nums[left]
        left += 1
      right += 1
    return res if res <= len(nums) else 0