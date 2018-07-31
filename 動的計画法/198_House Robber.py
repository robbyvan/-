# 198_House Robber
# 对于一个房子, 有抢或不抢两种状态
# 考虑rob[i]表示对于房子i: max(在i以前的以抢结尾的最大值, 抢房子i)
# skip[i]表示对于房子i: max(在i以前以不抢结尾的最大值, 不抢房子i)


class Solution:
  def rob(self, nums):
    if not nums:
      return 0
    rob, skip = nums[0], 0
    for i in range(1, len(nums)):
      prevRob = rob
      rob = max(rob, skip + nums[i])
      skip = max(skip, prevRob)
    return max(rob, skip)