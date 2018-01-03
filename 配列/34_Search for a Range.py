# 34_Search for a Range
# 两次二分查找, 第一次的low是左边
# 第二次找target + 1的low, 这是比target大1的位置, 所以结果在他们之间.
# 如果第一次target就不在, 那么是[-1, -1]
# 注意二分的high

class Solution:
  def searchRange(self, nums, target):
    def search(n):
      low, high = 0, len(nums)
      while low < high:
        mid = low + (high - low) / 2
        if nums[mid] >= n:
          high = mid
        else:
          low = mid + 1
      return low
    low = search(target)
    return [low, search(target + 1) - 1] if target in nums[low:low + 1] else [-1, -1]