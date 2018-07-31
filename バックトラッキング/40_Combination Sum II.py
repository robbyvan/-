# 40_Combination Sum II: candidates可重复, 但结果每个数字只能用一次
# 去重? candidates.sort() 按照顺序扫, 如果发现了数A后面的重复数A, 在扫到数A时, 都要跳过. 
# 后面数A的解集一定是之前数A的子集. (解集只用了2个数A, 三个连续的数A, 第一个A还可以空余1个出来)

class Solution:
  def combinationSum2(self, candidates, target):
    candidates.sort()
    res = []
    self.helper(candidates, 0, target, [], res)
    return res

  def helper(self, candidates, index, target, path, res):
    if target == 0:
      res.append(path)
      return
    for i in range(index, len(candidates)):
      if i != index and candidates[i] == candidates[index - 1]:
        continue
      elif target - candidates[i] >= 0:
        self.helper(candidates, index + 1, target - candidates[i], path + [candidates[i]], res)