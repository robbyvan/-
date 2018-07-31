# 446_Arithmetic Slices II - Subsequence
# 双重循环, 对于一个新的A[k], 0 -> k之间的所有数字都尝试一次, 计算diff = A[k] - A[i], 然后找到可能存在的开头A[i] - diff(*)
# 找到可能存在的开头A[i] - diff: 在lookup当中找, 有且index < i, 那么(k, diff) += 1 (只是三个数字k, i, i-diff的组合数)
# 所有的diff找完后, 更新(k, diff) = (k, diff) + (i, diff) k之前的上1个i, 满足diff的所有组合, 都可以再补一个k
# 返回所有坐标处所有diff总和

class Solution:
  def numberOfArithmeticSlices(self, A):
    lookup = {}
    for i, num in enumerate(A):
      if num in lookup:
        lookup[num].append(i)
      else:
        lookup[num] = [i]

    dp = []
    for _ in range(len(A)):
      dp.append({})

    for k, num in enumerate(A):
      for i in range(k):
        diff = num - A[i]
        X = A[i] - diff
        if X in lookup:
          for index in lookup[X]:
            if index < i:
              dp[k][diff] = dp[k].get(diff, 0) + 1

        if diff in dp[i]:
          dp[k][diff] = dp[k].get(diff, 0) + dp[i][diff]

    res = 0
    for num in dp:
      for diff in num:
        res += num[diff]
    return res
