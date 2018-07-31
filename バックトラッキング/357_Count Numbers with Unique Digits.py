# 357_Count Numbers with Unique Digits
# dp: 新的最高位 = 连乘 + 之前的数目 => 总的数目

class Solution:
  def countNumbersWithUniqueDigits(self, n):
    choice = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    m = min(10, n)
    # dp = [1] + [0] * m
    ans, newDigit = 1, 1
    for i in range(m):
      newDigit = choice[i] * newDigit
      ans = newDigit + ans
    return ans
