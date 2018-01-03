# 283_Move Zeroes
# 双指针, 一个记录0, 一个记录遍历
# 每遇到非0, 就交换二者位置, 并更新0指针位置
# 遍历指针结束后, 所有数字都已进行过排序
class Solution:
  def moveZeroes(self, nums):
    zero = 0
    for i in range(len(nums)):
      if nums[i] != 0:
        nums[i], nums[zero] = nums[zero], nums[i]
        zero += 1