# # 45. Jump Game II
# dp复杂度是O(n²)
# 考虑贪心, 每次跳最远一步, 然后这一大步里面的所有点决定了下一次跳的最大步
# 看一共可以几大步跳完.

class Solution:
  def jump(self, nums):
    steps = 0
    maxRange = 0
    stepEnd = 0
    for i in range(len(nums) - 1):
      maxRange = max(maxRange, nums[i] + i)
      if i == stepEnd:
        stepEnd = maxRange
        steps += 1
    return steps

# class Solution:
#   def jump(self, nums):
#     if len(nums) < 2:
#       return 0
#     dp = []
#     dp.append(0)
#     for i in range(1, len(nums)):
#       dp.append(-1)
#       for j in range(0, i):
#         if dp[j] != -1 and nums[j] + j >= i:
#           if dp[i] == -1:
#             dp[i] = dp[j] + 1
#           else:
#             dp[i] = min(dp[j] + 1, dp[i])
#     return dp[-1]