# 464_Can I Win
# DFS + memo, 基本情况:
#  1) 查看memo当前选择是否遇到过, 如果有memo, 返回
#  2) 新的情况, 对所有的可选数字, 进行选择
#  3) 如果选的数字i >= total, 这次选择能赢, 或者选i, 查看另一人self.helper(path, total - i)是不是输
#  4) 能赢 => 存入memo, 返回true
#  5) 不能赢 => 存入memo, 返回false

class Solution:
  def canIWin(self, maxChoosableInteger, desiredTotal):
    if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
      return False
    self.memo = {}
    path = ["0"] * (maxChoosableInteger + 1)
    return self.helper(path, desiredTotal)

  def helper(self, path, total):
    s = "".join(path)
    if s in self.memo:
      return self.memo[s]

    for i in range(1, len(path)):
      if path[i] == "0":
        path[i] = "1"
        if i >= total or not self.helper(path, total - i):
          path[i] = "0"
          self.memo[s] = True
          return True
        path[i] = "0"

    self.memo[s] = False
    return False