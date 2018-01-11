# 20_Valid Parentheses
# 利用dict保存括号对.
# 左括号入栈, 右括号检查栈顶即可.

class Solution:
  def isValid(self, s):
    d = {"(": ")", "[": "]", "{": "}"}
    left = "([{"
    stack = []
    for char in s:
      if char in left:
        stack.append(char)
      else:
        if not stack:
          return False
        peak = stack.pop()
        if d[peak] != char:
          return False
    return True if len(stack) == 0 else False

