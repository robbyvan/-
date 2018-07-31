# 87_Scramble String
# 见字符串87

class Solution:
  def isScramble(self, s1, s2):
    if len(s1) != len(s2):
      return False
    if sorted(s1) != sorted(s2) :
      return False
    if s1 == s2 or len(s1) < 4:
      return True

    for cut in range(1, len(s1)):
      if self.isScramble(s1[:cut], s2[:cut]) and self.isScramble(s1[cut:], s2[cut:]):
        return True
      if self.isScramble(s1[:cut], s2[-cut:]) and self.isScramble(s1[cut:], s2[:-cut]):
        return True
    return False
