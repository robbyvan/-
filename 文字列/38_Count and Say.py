# 38. Count and Say
# 按照定义, 变量:
# 外层: 趟数step, 上次结果s, 
# 内层: 当前字符curr, 计数count, 本趟结果res.
# 每趟开始的时候, 设置s[0]为初始化(curr, count), 每趟结束时手动添加最后一个curr count.

class Solution:
  def countAndSay(self, n):
    if n <= 0:
      return ""
    s = "1"
    step = 1
    while step < n:
      res = ""
      curr = s[0]
      count = 1
      for i in range(1, len(s)):
        if s[i] == curr:
          count += 1
        else:
          res = res + str(count) + curr
          curr = s[i]
          count = 1
      res = res + str(count) + curr
      s = res
      step += 1
    return s



