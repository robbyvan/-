# 43_Multiply Strings
# 按照竖乘定义.结果是l1 + l2大小.初始化全0
# 两层循环, 外层l1 -> 0, 内层l2 -> 0
# 内层开始, 初始carry = 0. 当前位(res[i + j + 1])求%, 进位(carry)求/. 
# 直到循环结束, 对应的res[i](此时j = 0, 当前位i + j + 1 = i + 1, 前一位就是i)处+剩下的carry.

class Solution:
  def multiply(self, num1, num2):
    res = [0] * (len(num1) + len(num2))
    for i in range(len(num1) - 1, -1, -1):
      carry = 0
      for j in range(len(num2) - 1, -1, -1):
        temp = int(num1[i] ) * int(num2[j]) + carry
        carry = (res[i + j + 1] + temp) // 10
        res[i + j + 1] = (res[i + j + 1] + temp) % 10
      res[i] += carry
    res = "".join(map(str, res))
    return "0" if not res.lstrip("0") else res.lstrip("0")
