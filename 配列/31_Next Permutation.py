# 31_Next Permutation
# 找到最右的一个极大值点, 找到极大值点最小的比极大值左边小的数字(因为一定是递减的, 所以从右开始找到第一个就好了)
# 如果不存在, 直接翻转全部数组.
# 交换两个数字, reverse二者之间的部分
class Solution:
  def nextPermutation(self, nums):
    right = len(nums) - 1
    while right >= 1 and nums[right] <= nums[right - 1]:
      right -= 1
      if right == 0:
        self.reverse(nums, 0, len(nums) - 1)
        return
    left = right - 1
    s = 0
    for i in range(len(nums) - 1, left, -1):
      if nums[i] > nums[left]:
        s = i
        # 因为一定是递减的, 所以找到第一个就好了
        break
    nums[left], nums[s] = nums[s], nums[left]
    self.reverse(nums, left + 1, len(nums) - 1)

  def reverse(self, nums, l, r):
    while l < r:
      nums[l], nums[r] = nums[r], nums[l]
      l += 1
      r -= 1

