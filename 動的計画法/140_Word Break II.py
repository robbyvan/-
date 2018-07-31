# 140_Word Break II
# DFS + memo, top-down解决

class Solution:
  def wordBreak(self, s, wordDict):
    self.memo = {}
    return self.helper(s, len(s) - 1, wordDict)

  def helper(self, s, index, wordDict):
    if index == len(s):
      return []
    if index in self.memo:
      return self.memo[index]

    res = []
    for w in wordDict:
      if s[index + 1 - len(w):index + 1] == w:
        if index + 1 - len(w) == 0:
          res.append(w)
        elif index + 1 - len(w) > 0:
          prev = self.helper(s, index - len(w), wordDict)
          for ans in prev:
            res.append(ans + " " + w)
    self.memo[index] = res
    return res