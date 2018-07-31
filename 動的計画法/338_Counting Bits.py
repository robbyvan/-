# 338_Counting Bits
# 每次遇到了1, 2, 4, 8, 16...是bit单1的情况时, 后面的数字是在重复之前的组合 + 1(首位)

class Solution:
  def countBits(self, num):
    res = [0] * (num + 1)
    lastMagBit = 1
    for i in range(1, num + 1):
      if i == lastMagBit * 2:
        lastMagBit *= 2
      res[i] = res[i - lastMagBit] + 1
    return res