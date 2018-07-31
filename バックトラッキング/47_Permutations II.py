# 47_Permutations II
# source有重复数字时, 只要保证在特定的位上, 出现数字A的情况仅有一次即可.
# 利用set保存这一位的使用情况, 填字前查重

class Solution:
  def permuteUnique(self, nums):
    if not nums:
      return []
    res = []
    self.helper(nums, [], res)
    return res

  def helper(self, source, path, res):
    if not source:
      res.append(path)
      return 

    used = set()
    for i in range(len(source)):
      if source[i] not in used:
        used.add(source[i])
        self.helper(source[:i] + source[i + 1:], path + [source[i]], res)