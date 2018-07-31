# 494_Target Sum
# DFS + memo
# BFS. 每次遇到一个新的数字 => 对上层所有的和, 加减nums[i], 成为新的层 => 最后一层找dp[S]

class Solution:
  def findTargetSumWays(self, nums, S):
    if not nums:
      return 0
    q = {}
    if nums[0] == 0:
      q[0] = 2
    else:
      q[nums[0]], q[-nums[0]] = 1, 1

    for i in range(1, len(nums)):
      nextQ = collections.defaultdict(int)
      for key in q:
        nextQ[ key + nums[i]] += q[key]
        nextQ[ key - nums[i]] += q[key]
      q = nextQ
    return q.get(S, 0)


# class Solution:
#   def findTargetSumWays(self, nums, S):
#     if not nums:
#       return 0
#     self.memo = {}
#     return self.helper(nums, 0, 0, S)

#   def helper(self, nums, index, path, target):
#     if (index, path) in self.memo:
#       return self.memo[(index, path)]

#     if index == len(nums):
#       if path == target:
#         return 1
#       return 0

#     add = self.helper(nums, index + 1, path + nums[index], target)
#     subtract = self.helper(nums, index + 1, path - nums[index], target)
#     self.memo[(index, path)] = add + subtract
#     return (add + subtract)