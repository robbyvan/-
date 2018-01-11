# 30_Substring with Concatenation of All Words
# 按照定义. 创建目标counter
# 从头开始按单词长度扫描, 扫够n个单词, 对比seen和counter是否相同, 相同则找到, 返回.
import collections
class Solution:
  def findSubstring(self, s, words):
    wordBag = collections.Counter(words)
    wordLen, numWords = len(words[0]), len(words)
    totalLen, res = wordLen * numWords, []
    for i in range(len(s) - totalLen + 1):
      seen = collections.defaultdict(int)
      for j in range(i, i + totalLen, wordLen):
        currWord = s[j:j + wordLen]
        if currWord in wordBag:
          seen[currWord] += 1
          if seen[currWord] > wordBag[currWord]:
            break
        else:
          break
      if seen == wordBag:
        res.append(i)
    return res


