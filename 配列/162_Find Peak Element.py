# 162.Find Peak Element
# 二分搜索, 使用2个mid, mid2 = mid1 + 1, 更新low和high, 返回low
class Solution:
  def findPeakElement(self, nums):
    low, high = 0, len(nums) - 1
    while low < high:
      mid1 = low + (high - low) / 2
      mid2 = mid1 + 1
      if nums[mid1] < nums[mid2]:
        low = mid2
      else:
        high = mid1

    return low