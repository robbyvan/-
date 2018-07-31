# 401_Binary Watch
# 划分x, y个点构成H, M => 找到所有的x构成的H, y构成的M


class Solution:
  def readBinaryWatch(self, n):
    res = []
    for i in range(n + 1):
      hours = self.getHour(i)
      if len(hours) == 0:
        continue
      minutes = self.getMin(n - i)
      if len(minutes) != 0:
        res += [h + ":" + m for h in hours for m in minutes]
    return res

  def getHour(self, n):
    def helper(source, n, path, res):
      if path > 11:
        return 
      if n == 0:
        res.append(str(path))
        return
      for i in range(len(source)):
        helper(source[i + 1:], n - 1, path + source[i], res)

    res = []
    if n > 3:
      return res
    helper([1, 2, 4, 8], n, 0, res)
    return res

  def getMin(self, n):
      def helper(source, n, path, res):
        if path > 59:
          return
        if n == 0:
          if path < 10:
            res.append("0" + str(path))
          else:
            res.append(str(path))
          return
        for i in range(len(source)):
          helper(source[i + 1:], n - 1, path + source[i], res)
      res = []
      if n > 5:
        return res
      helper([1, 2, 4, 8, 16, 32], n, 0, res)
      return res