# 526_Beautiful Arrangement
# DFS + memo
# 利用tuple存储source + index作为key

class Solution:
  def countArrangement(self, n):
    source = tuple(range(1, n + 1))
    self.memo = {}
    return self.helper(source, n)

  def helper(self, source, index):
    if index < 1:
      return 1
    key = (source, index)
    if key in self.memo:
      return self.memo[key]

    count = 0
    for i in range(len(source)):
      if source[i] % index == 0 or index % source[i] == 0:
        count = count + self.helper(source[:i] + source[i + 1:], index - 1)
    self.memo[key] = count
    return count

# class Solution:
#   def countArrangement(self, n):
#     if n < 1:
#       return 0
#     source = [i for i in range(1, n + 1)]
#     res = [0]
#     self.helper(source, n, n, res)
#     return res[0]

#   def helper(self, source, i, n, res):
#     if i < 1:
#       res[0] += 1
#       return
#     for j, num in enumerate(source):
#       if num % i == 0 or i % num == 0:
#         self.helper(source[:j] + source[j + 1:], i - 1, n, res)
