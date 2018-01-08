# 520_Detect Capital
# 一个思路: 是否等于全大写, 是否等于全小写, 是否第一个字母外等于全小写

class Solution:
  def detectCapitalUse(self, word):
    return word.isupper() or word.islower() or word.istitle()