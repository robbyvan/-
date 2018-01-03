# 26.Remove Duplicates from Sorted Array
# 双指针, 一个遍历, 一个空位
# 如果遍历处是第一个 或者不是重复, 那么就移动到空位, 更新空位
# 否则跳过这个点, 这个点将成为空位.
class Solution:
  def removeDuplicates(self, nums):
    if not nums:
      return 0
    i = 0
    for num in nums:
      if i == 0 or num > nums[i - 1]:
        nums[i] = num
        i += 1
    return i