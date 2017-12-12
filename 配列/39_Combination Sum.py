# 39. Combination Sum
# 回溯
# 求target能不能拆成sum之和, 每个数字变成加数进行试探 => 
# 1) 小了: 继续拆
# 2) 大了: 舍弃当前数字, 返回上一个状态
# 3) 相等: 加入解
# 数组先经过排序, 和循环起点index一起完成了去重

class Solution:
  def combinationSum(self, candidates, target):
    candidates.sort()
    res = []
    self.dfs(candidates, target, 0, [], res)
    return res
  def dfs(self, candidates, target, index, path, res):
    if target < 0:
      return
    if target == 0:
      res.append(path)
      return
    for i in range(index, len(candidates)):
      self.dfs(candidates, target - candidates[i], i, path + [candidates[i]], res)