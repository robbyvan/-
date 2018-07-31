# 17_Letter Combinations of a Phone Number
# 寻找一条路径, 从头 => 尾, 每个节点都有分支

class Solution:
  def letterCombinations(self, digits):
    if not digits or len(digits) == 0:
      return []
    res = []
    self.helper(digits, "", res)
    return res

  def helper(self, source, path, res):
    lookup = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    if not source:
      res.append(path)
      return
    num = source[0]
    if num in lookup:
      for ch in lookup[num]:
        self.helper(source[1:], path + ch, res)