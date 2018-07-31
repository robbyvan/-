# 216_Combination Sum III: 找k个数使得sum = n. 只能从1~9选, 而且每个数只能用一次
# 去重: 考虑遍历方式, 取了i时, 下次只能用i以后的数字组成答案 (每个i, 答案以i开头)

class Solution:
  def combinationSum3(self, k, n):
    source = [i for i in range(1, 10)]
    res = []
    self.helper(source, k, n, [], res)
    return res

  def helper(self, source, k, target, path, res):
    if k == 0 and target != 0:
      return
    if k == 0 and target == 0:
      res.append(path)
      return
    for i in range(len(source)):
      if target - source[i] >= 0:
        self.helper(source[i + 1:], k - 1, target - source[i], path + [source[i]], res)