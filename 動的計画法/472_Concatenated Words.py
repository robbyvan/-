# 472_Concatenated Words
# dfs, 按照定义分成两块, 同时满足要求即可(if word[:cut] in wordList and helper(word[cut:]): return True)
# 要求一定分成两块? => 先按照长度sort词, 从短到长检验, 再往set里添加该词
# 保证对于word in wordList的情况, 基本词是false, 组合词是true

class Solution(object):
  def findAllConcatenatedWordsInADict(self, words):
    words = sorted(words, key = lambda t: len(t))
    wordList = set()
    def helper(word):
      if word in wordList:
        return True
      for cut in range(1, len(word)):
        if word[:cut] in wordList and helper(word[cut:]):
          return True
      return False
    res = []
    for word in words:
      if helper(word):
        res.append(word)
      wordList.add(word)
    return res
