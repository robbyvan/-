# 413_Arithmetic Slices
# Slices是连续的段.
# (i, j) => (i, j + 1) = (i, j) + △
# 其中△是从left开始一直到含j直到只剩3位的组合数

class Solution:
  def numberOfArithmeticSlices(self, A):
    if not A:
      return 0
    dp, k = [0] * len(A), 1
    for i in range(2, len(A)):
      if A[i] + A[i - 2] == A[i - 1] + A[i - 1]:
        dp[i] = dp[i - 1] + k
        k += 1
      else:
        dp[i] = dp[i - 1]
        k = 1
    return dp[-1]