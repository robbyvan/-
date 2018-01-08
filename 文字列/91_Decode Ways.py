# 91. Decode Ways
# 从右向左decode.
# i处遇到一个非0数字, 如果[i:i+2]可以小于26, 说明有2中方式, 所以是opt[i+1] + opt[i+2]
# 如果大于26, 只可能是opt[i+1] (i单独出来唯一一种)
# 如果i处遇到0, 这时候对于[i-1:i+1] 一定是x0单独出来, 是新i的opt[i + 2].
# 但是处理的时候把0处的opt = 0, 就也能写成opt[i+1](=0) + opt[i+2]



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