# 214_Shortest Palindrome
# 基本思路: 找到原串s最长的回文前缀.补上剩余部分的逆即可.
# 倒置s得到逆串r, 从0开始cut串r, 直到首次遇见r[cut:]是s的开头部分(就是最长的回文前缀)
# 返回r[:cut] + s即可
class Solution:
  def shortestPalindrome(self, s):
    r = s[::-1]
    for cut in range(len(r) + 1):
      if s.startswith(r[cut:]):
        return r[:cut] + s
