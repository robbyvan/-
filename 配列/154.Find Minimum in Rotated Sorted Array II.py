# 154.Find Minimum in Rotated Sorted Array II
# 考虑了有重复数字的情况
# 重复数字会影响的情况为当重复数字出现在两头, 导致二分的时候有可能选择了错误的一边
# 因此要让开始二分时的两端的数字存在大小差异
# 在二分前, 通过循环去掉两端的重复. low++ 或者 high-- 直到low, high不等.
class Solution:
  def findMin(self, nums):
    low, high = 0, len(nums) - 1

    while nums[low] == nums[high] and high > low:
      high -= 1

    while low < high:
      mid = low + (high - low) / 2
      if nums[mid] > nums[high]:
        low = mid + 1
      else:
        high = mid

    return nums[low]