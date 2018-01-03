# 35. Search Insert Position
# 类似34, 这里high取len(nums), 因为只用访问nums[mid].
# 如果mid >= target, 更新high, 否则更新low

class Solution:
  def searchInsert(self, nums, target):
    if not nums:
      return 0
    low, high = 0, len(nums)
    while low < high:
      mid = low + (high - low) / 2
      if nums[mid] >= target:
        high = mid
      else:
        low = mid + 1
    return low
