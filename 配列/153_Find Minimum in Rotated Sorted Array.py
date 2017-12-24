# 153.Find Minimum in Rotated Sorted Array
# 二分搜索, 偏移的有序数组不再是单调的, 找到单调性改变的地方即可.

class Solution: 
  def findMin(self, nums):
    low, high = 0, len(nums) - 1
    while low < high:
      mid = low + (high - low) / 2
      if nums[mid] > nums[high]:
        low = mid + 1
      else:
        high = mid
    return nums[low]