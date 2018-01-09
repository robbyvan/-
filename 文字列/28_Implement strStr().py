# 28_Implement strStr()
# 暴利比较haystack长度为n的子串和needle是否相同.
class Solution: 
  def strStr(self, haystack, needle):
    m, n = len(haystack), len(needle)
    if m < n:
      return -1
    elif n == 0:
      return 0

    for i in range(m - n + 1):
      if haystack[i:i + n] == needle:
        return i
    return -1
