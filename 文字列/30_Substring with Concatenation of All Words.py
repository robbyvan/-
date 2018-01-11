# 30_Substring with Concatenation of All Words
# 按照定义. 创建目标counter
# 从头开始按单词长度扫描, 扫够n个单词, 对比seen和counter是否相同, 相同则找到, 返回.
import collections
class Solution:
  def findSubstring(self, s, words):
    res = []
    if not words:
      return []
    wordLen, wordNum = len(words[0]), len(words)
    totalLen = wordLen * wordNum
    targets = collections.Counter(words)
    for i in range(len(s) - totalLen + 1):
      seen = collections.defaultdict(int)
      for j in range(i, i + totalLen, wordLen):
        curr = s[j:j + wordLen]
        if curr in targets:
          seen[curr] += 1
          if seen[curr] > targets[curr]:
            break
        else:
          break
      if seen == targets:
        res.append(i)
    return res