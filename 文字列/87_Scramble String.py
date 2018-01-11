# 87_Scramble String
# 按照递归定义解
# 如果word1, word2分别A1, B1; A2, B2已经解决
# 那么只要对于任意非空cut: 有[A1, A2] + [B1, B2] 或者[A1, B2] + [A2, B1]任意一项成立即可(scramble的定义, 交换前后)
# 优化: 长度小于4的词, 所有全排列都是True

class Solution:
  def isScramble(self, s1, s2):
    m, n = len(s1), len(s2)
    if m != n or sorted(s1) != sorted(s2):
      return False
    if s1 == s2 or m < 4:
      return True

    for cut in range(1, m):
      if self.isScramble(s1[:cut], s2[:cut]) and self.isScramble(s1[cut:], s2[cut:]):
        return True
      if self.isScramble(s1[:cut], s2[-cut:]) and self.isScramble(s1[cut:], s2[:-cut]):
        return True

    return False
