# 66_Plus One
# 倒序遍历 + 1
class Solution:
  def plusOne(self, digits):
    add = False
    for right in range(len(digits) - 1, -1, -1):
      res = digits[right] + 1
      if res < 10:
        add = False
        digits[right] = res
        break
      else:
        digits[right] = 0
        add = True
    return [1] + digits if add else digits


