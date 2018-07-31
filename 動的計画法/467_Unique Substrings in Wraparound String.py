# 467_Unique Substrings in Wraparound String
# 是循环重复的字符串, 考虑26个字母结尾, 分别的最长合法串的长度.
# eg: 对"zabc"和"abc", 所有"abc"能组成的答案, "zabc"一定有

class Solution:
  def findSubstringInWraproundString(self, p):
    if not p:
      return 0
    if len(p) == 1:
      return 1
    memo = [0] * 26
    prev, start  = p[0], 0
    memo[ord(prev) - ord("a")] = 1
    for i in range(1, len(p)):
      ch = p[i]
      if prev + ch != "za" and ord(ch) - ord(prev) != 1:
        start = i
      memo[ord(ch) - ord("a")] = max(memo[ord(ch) - ord("a")], i - start + 1)
      prev = ch
    return sum(memo)

a = Solution().findSubstringInWraproundString("cabc")
print(a)

