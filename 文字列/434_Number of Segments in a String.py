# 434_Number of Segments in a String
# 按照定义, 首先过掉空格, 如果还在len内, 遇到第一个非空格+1, 过掉所有非空格.
# 或者计数规则: 遇到了space, 如果之前是字符 + 1; 遇到了结尾, 检查当前或者之前是否是字符 + 1

class Solution:
  def countSegments(self, s):
    if not s:
      return 0
    p, count = 0, 0
    while p < len(s):
      while p < len(s) and s[p].isspace():
        p += 1
      if p < len(s):
        count += 1
      while p < len(s) and not s[p].isspace():
        p += 1
    return count

# class Solution:
#   def countSegments(self, s):
#     if not s:
#       return 0
#     count = 0
#     metChar = False
#     for i in range(len(s)):
#       if s[i].isspace():
#         if metChar:
#           count += 1
#           metChar = False
#       elif i == len(s) - 1:
#         if metChar or not s[i].isspace():
#           count += 1
#       else:
#         metChar = True
#     return count
