# 392_Is Subsequence
# 双指针, 按顺序能拼出s即true

class Solution:
  def isSubsequence(self, s, t):
    m, n = len(t), len(s)
    if m < n:
      return False
    if n == 0:
      return True
    ps, pt = 0, 0
    while pt < m:
      if t[pt] == s[ps]:
        ps += 1
      if ps == n:
        return True
      pt += 1
    return False
