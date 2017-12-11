# 16. 3Sum Closest
# 和15相同, 但内层条件的[加入解]为: 相等直接return, 不相等时, 如果缩小了绝对差就更新解.
class Solution:
  def threeSumClosest(self, nums, target):
    nums.sort()
    length = len(nums)
    result = float("inf")
    for i in range (0, length - 2):
      if i and nums[i] == nums[i - 1]:
          continue
      left, right = i + 1, length - 1
      while left < right:
        s = nums[i] + nums[left] + nums[right]
        if s == target:
          return s
        if abs(s - target) < abs(result - target):
          result = s
        if s > target:
          right -= 1
        elif s < target:
          left += 1
    return result