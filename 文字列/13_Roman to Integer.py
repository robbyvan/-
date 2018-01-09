# 13_Roman to Integer
# 按照定义累加, 罗马数字, 如果小的放在大的左边, 那么就是减

class Solution:
  def romanToInt(self, s):
    roman = { 'I': 1, 'X': 10, 'C': 100, 'M': 1000, 'V': 5, 'L': 50, 'D': 500 }
    res = 0
    for i in range(len(s) - 1):
      if roman[s[i]] < roman[s[i + 1]]:
        res = res - roman[s[i]]
      else:
        res = res + roman[s[i]]
    return res + roman[s[-1]]