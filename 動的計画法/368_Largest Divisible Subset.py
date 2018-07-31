# 368_Largest Divisible Subset
# 不仅要DP求出最大的组合数目, 还要找出一个这样的组合(倒推)
# 排序nums, 考虑数i, opt[i] = max(opt[k] + 1) { 0<= k <= i - 1}
# 对于全局, 利用maxVal和end记录最大的组合数和最大子序列的结尾数字坐标(用于倒推出序列)
# 在上面更新最大组合数的同时, 记录下上一个数字的位置.

class Solution:
  def largestDivisibleSubset(self, nums):
    if not nums:
      return []
    nums.sort()
    n = len(nums)
    prev, dp = [-1] * n, [0] * n
    maxVal, end = 0, -1

    for i in range(n):
      dp[i], prev[i] = 1, -1
      for j in range(i - 1, -1, -1):
        if nums[i] % nums[j] == 0:
          if dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            prev[i] = j
      if dp[i] > maxVal:
        maxVal = dp[i]
        end = i

    res = []
    while end != -1:
      res.append(nums[end])
      end = prev[end]

    return res