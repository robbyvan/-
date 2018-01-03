# 80_Remove Duplicates from Sorted Array II
# 类似26, 只用把交换条件改成2个的情况, 如果小于2, 或者等于前1(2)个
class Solution:
  def removeDuplicates(self, nums):
    tail = 0
    for num in nums:
      if tail < 2 or num != nums[tail - 1] or num != nums[tail - 2]:
        nums[tail] = num
        tail += 1
    return tail
