# 357_Count Numbers with Unique Digits
# 首位可选1~9, 次位可选9种, 之后依次少1可选项, 
# 单独的0额外计算

class Solution:
  def countNumbersWithUniqueDigits(self, n):
    if n < 0:
      return 0
    choices = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    ans, prod = 1, 1
    for i in range(n if n < 10 else 10):
      prod = prod * choices[i]
      ans += prod
    return ans

    



