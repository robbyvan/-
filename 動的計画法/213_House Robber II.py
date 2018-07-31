# 213_House Robber II
# 抢头, 不抢头, 分别按照之前的方法操作一次

class Solution:
  def rob(self, nums):
    if not nums:
      return 0
    if len(nums) == 1:
      return nums[0]

    rob, skip = 0, 0
    for i in range(len(nums) - 1):
      prevRob = rob
      rob, skip = max(skip + nums[i], rob), max(skip, prevRob)
    robHead = max(rob, skip)

    rob, skip = 0, 0
    for i in range(1, len(nums)):
      prevRob = rob
      rob, skip = max(skip + nums[i], rob), max(skip, prevRob)
    skipHead = max(rob, skip)

    return max(robHead, skipHead)

