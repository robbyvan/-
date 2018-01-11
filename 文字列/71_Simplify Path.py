# 71_Simplify Path
# 按照定义即可.先按照"/+"split, 然后遍历
# "" & "."不管
# ".." 在非空时pop()
# 其他直接append()

import re
class Solution:
  def simplifyPath(self, path):
    paths = re.split('/+', path)
    stack = []
    for ch in paths:
      if ch == '' or ch == '.':
        continue
      elif ch == '..':
        if len(stack) > 0:
          stack.pop()
      else:
        stack.append(ch)

    if len(stack) == 0:
      return '/'
    res = ''
    for folder in stack:
      res = res + '/' + folder
    return res