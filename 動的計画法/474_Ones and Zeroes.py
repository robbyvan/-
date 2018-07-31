# 474_Ones and Zeroes
# 考虑01背包
# 背包: 限重, 物品数 => 价值: opt(k, w) = max(opt(k - 1, w - wk) + vk, opt(k, w - wk))
# 01字符串: 0/1个数, 物品限定范围(前k个)  => 最多选择
# opt(i, j, k) = max(opt(i, j, k - 1), opt(i - z, j - o, k - 1) + 1)
# 必须在循环的时候使m, n从[满 -> 0]. why?? (虽然感觉上来说对新词, 拉满m, n才是起始状态)

class Solution:
  def findMaxForm(self, strs, m, n):
    def count(s):
      return sum(1 for c in s if c == "0"), sum(1 for c in s if c == "1")

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for numstr in strs:
      z, o = count(numstr)
      for i in range(m, -1, -1):
        for j in range(n, -1, -1):
          if i >= z and j >= o:
            dp[i][j] = max(dp[i - z][j - o] + 1, dp[i][j])

    return dp[m][n]