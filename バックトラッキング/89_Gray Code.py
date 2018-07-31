# 89_Gray Code
# 利用BFS. 原理: 每次只能改变一位 => 同层内, 结点都是相差1, 转换结点的时候, 保持新位是相同的
# 在同一位内生成"0""1"的后缀

class Solution:
  def grayCode(self, n):
    if n == 0:
      return 0
    q = ["0", "1"]
    digit = 1
    while digit < n:
      nextQ = []
      lastBit = "0"
      for node in q:
        if lastBit == "0":
          nextQ.append(node + "0")
          nextQ.append(node + "1")
          lastBit = "1"
        else:
          nextQ.append(node + "1")
          nextQ.append(node + "0")
          lastBit = "0"
      q = nextQ
      digit += 1
    return [int(num, 2) for num in q]

a = Solution().grayCode(1)
print(a)