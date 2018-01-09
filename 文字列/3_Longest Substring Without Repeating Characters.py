# 3_Longest Substring Without Repeating Characters
# 扫描一次, 每当遇到已有的(全局已有)字符, 找到上次出现的位置(必须满足在这一段内已出现过) 求差得到当前长度
# 每遇到一个字母都更新maxLen和d{}

class Solution(object):
  def lengthOfLongestSubstring(self, s):
    start, count = 0, 0
    d = {}
    for i, char in enumerate(s):
      if char in d and start <= d[char]:
        start = d[char] + 1
      count = max(count, i - start + 1)
      d[char] = i
    return count

