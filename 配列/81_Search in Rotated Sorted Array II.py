# 81_Search in Rotated Sorted Array II
# 二分搜索
# mid == target, 找到 返回True
# 否则检查mid和high的关系, 确定rotate了是否过半
# 如果mid > high, 那么rotate过半了, 所以查前半部分, 看是否target落在low和mid之间, 是=>high = mid否则low = mid + 1
# 如果mid < high, 那么rotate没过半, 所以查后半部分, 看target和mid high.落在之间: low = mid + 1否则high = mid
# 如果mid == high了.说明有duplicates, 删掉末尾, high--
# 最终while完毕之后, 返回low, 检查low是不是target.
class Solution:
  def search(self, nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
      mid = (low + high) / 2
      if nums[mid] == target:
        return True
      if nums[mid] > nums[high]:
        if nums[mid] > target and nums[low] <= target:
          high = mid
        else:
          low = mid + 1
      elif nums[mid] < nums[high]:
        if nums[mid] < target  and nums[high] >= target:
          low = mid + 1
        else:
          high = mid
      else:
        high -= 1
    return True if nums[low] == target else False


