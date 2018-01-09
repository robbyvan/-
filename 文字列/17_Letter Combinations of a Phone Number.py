# 17_Letter Combinations of a Phone Number
# 利用helper, 寻找所有路径.
# helper中, 每次添加一位数的所有组合进入path, 消耗完digits就找到了一条path. 添加进res.

# class Solution(object):
#   def letterCombinations(self, digits):
#     if '' == digits:
#       return []
#     kvmaps = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
#     return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])

class Solution:
  def letterCombinations(self, digits):
    if not digits or len(digits) == 0:
      return []
    res = []
    self.helper(res, "", digits)
    return res

  def helper(self, res, path, digits):
    keyboard = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    if not digits or len(digits) == 0:
      return
    if len(digits) == 1 and int(digits) > 1:
      options = keyboard[digits]
      for i in range(len(options)):
        res.append(path + options[i])
      return
    curr = digits[0]
    options = keyboard[curr]
    for i in range(len(options)):
      self.helper(res, path + options[i], digits[1:])

