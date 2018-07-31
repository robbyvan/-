# 416_Partition Equal Subset Sum
# 类似背包问题, 对每个数字, 有要或不要两种抉择
# dp(k, target) = dp(k - 1, target) or dp(k - 1, target - Vk)
# k: 有几个数字可选 => 对应到字符串时, 有0个的情况, 因此补1, 需要初始化0个的情况
# target: 要求的组合之和 => 属于0~target(共target + 1个), 不用初始化

class Solution:
  def canPartition(self, nums):
    target = sum(nums)
    if target & 1 == 1:
      return False
    target = target // 2
    n = len(nums)

    dp = [[False] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for k in range(1, n + 1):
      for t in range(target + 1):
        if t >= nums[k - 1]:
          dp[k][t] = dp[k - 1][t] or dp[k - 1][t - nums[k - 1]]
        else:
          dp[k][t] = dp[k - 1][t]

    return dp[-1][-1]