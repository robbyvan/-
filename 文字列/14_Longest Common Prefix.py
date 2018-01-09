# 14_Longest Common Prefix
# 1) 使用reduce, 每次比较2个的公共长度.common会随着进行越来越小.
# 2) 使用全体比较, 每加一位, 就扫一遍所有字符串进行比较

class Solution:
  def longestCommonPrefix(self, strs):
    def lcp(s, t):
      if len(s) > len(t):
        s, t = t, s
      for i in range(len(s)):
        if s[i] != t[i]:
          return s[:i]
      return s
    return reduce(lcp, strs) if strs else ""
