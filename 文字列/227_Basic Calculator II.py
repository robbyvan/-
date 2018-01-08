# 227_Basic Calculator
# 按照定义进行加减乘除
# 利用stack存放每次运算后的结果.(因为有乘除)
# 注意除法处理负数结果, 因为有truncate所以两种情况.(有无余数)

class Solution:
  def calculate(self, s):
    if not s:
      return "0"
    num, sign, stack = 0, '+', []
    for i in range(len(s)):
      if s[i].isdigit():
        num = num * 10 + ord(s[i]) - ord("0")
      if (not s[i].isdigit() and not s[i].isspace()) or i == len(s) - 1:
        if sign == "+":
          stack.append(num)
        elif sign == "-":
          stack.append(-num)
        elif sign == "*":
          stack.append(stack.pop() * num)
        elif sign == "/":
          temp = stack.pop()
          if temp // num < 0 and temp % num != 0:
            stack.append(temp // num + 1)
          else:
            stack.append(temp // num)
        sign = s[i]
        num = 0
    return sum(stack)

