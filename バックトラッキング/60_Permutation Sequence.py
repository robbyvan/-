# 60_Permutation Sequence
# 迭代.从高位开始找, 基于0base: k = k - 1
# k // divisor[pos] => 找该位数字; k % k => 下一位的被除数; 利用pop()弹出用过的数字

class Solution:
  def getPermutation(self, n, k):
    divisors = [1] * (n)
    ans = 1
    for i in range(1, n):
      ans = ans * i
      divisors[i] = ans

    source = [i for i in range(1, n + 1)]
    res, pos = [], n - 1
    k -= 1
    while pos >= 0:
      index = k // divisors[pos]
      k = k % divisors[pos]
      res.append(source[index])
      source.pop(index)
      pos -= 1
    return "".join(str(num) for num in res)



# class Solution:
#   def getPermutation(self, n, k):
#     self.count, self.res = 0, []
#     source = [i for i in range(1, n + 1)]
#     self.helper(n, k, source, [])
#     return "".join(str(num) for num in self.res)

#   def helper(self, n, k, source, path):
#     if self.count == k:
#       return

#     if len(path) == n:
#       self.count += 1
#       if self.count == k:
#         self.res += path
#       return

#     # if len(path) < n
#     for i in range(len(source)):
#       curr = source[i]
#       if self.count < k:
#         self.helper(n, k, source[:i] + source[i + 1:], path + [curr])

a = Solution().getPermutation(3, 4)
print(a)