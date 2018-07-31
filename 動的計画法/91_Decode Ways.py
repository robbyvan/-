# 91_Decode Ways
# 见字符串91

class Solution(object):
  def numDecodings(self, s):
    if not s:
      return 0
    n = len(s)
    opt = [0 for _ in range(n + 1)]
    opt[n] = 1
    opt[n - 1] = 1 if s[n - 1] != '0' else 0

    for i in range(n - 2, -1, -1):
      if s[i] != '0':
        opt[i] = opt[i + 1] + opt[i + 2] if int(s[i:i + 2]) <= 26 else opt[i + 1]

    return opt[0]