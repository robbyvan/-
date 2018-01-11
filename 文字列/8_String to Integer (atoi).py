# 8_String to Integer (atoi)
# 删掉首位空白, strip()
# 确定sign, 如果ls[0] = '-', -1, 否则1
# 如果有+/-, 扔掉符号位
# 遍历加上每位
# 返回-2 ** 31 和 2 ** 31 之间的正解 return max(-2 ** 31, min(sign * res, 2 ** 31 -1))

class Solution:
  def myAtoi(self, s):
    if len(s) == 0:
      return 0
    ls = list(s.strip())
    sign = -1 if ls[0] == '-' else 1
    if ls[0] in ['-', '+']:
      ls.pop(0)
    res, i = 0, 0
    while i < len(ls) and ls[i].isdigit():
      res = res * 10 + ord(ls[i]) - ord('0')
      i += 1
    return max(-2 ** 31, min(sign * res, 2 ** 31 -1))