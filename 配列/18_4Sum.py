# 18. 4Sum
# 原理相同 多一个外层循环

class Solution:
  def fourSum(self, nums, target):
    nums.sort()
    length = len(nums)
    res = []
    for i in range(0, length - 3):
      if i and nums[i] == nums[i - 1]:
        continue
      for j in range(i + 1, length - 2):
        if j > (i + 1) and nums[j] == nums[j - 1]:
          continue
        left, right = j + 1, length - 1
        while left < right:
          s = nums[i] + nums[j] + nums[left] + nums[right]
          if s > target:
            right -= 1
          elif s < target:
            left += 1
          else: 
            res.append([nums[i], nums[j], nums[left], nums[right]])
            while left < right and nums[left] == nums[left + 1]:
              left += 1
            while left < right and nums[right] == nums[right - 1]:
              right -= 1
            left += 1
            right -= 1
    return res
