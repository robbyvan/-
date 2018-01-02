# 53. Maximum Subarray
# DP: 1~i-1 => 1~i, 但是因为只用关注dp[n], 因此只用一个res保存最大的答案

class Solution:
  def maxSubArray(self, A):
    if not A:
      return 0
    dp = A[0]
    res = A[0]
    for num in A[1:]:
      dp = max(num, dp + num)
      res = max(dp, res)
    return res

