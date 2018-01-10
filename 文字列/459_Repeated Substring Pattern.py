# 459_Repeated Substring Pattern
# 拼接两个, 删掉首尾, 找原串

class Solution:
  def repeatedSubstringPattern(self, s):
    if not s:
      return False
    ss = (s + s)[1:-1]
    return ss.find(s) != -1