# 140_Word Break II
#  DFS + memo
#  why memo? 解决sub-problem

class Solution:
  def wordBreak(self, s, wordDict):
    self.memo = {}
    return self.helper(s, len(s) - 1, wordDict)

  def helper(self, source, index, wordDict):
    if index in self.memo:
      return self.memo[index]

    res = []
    for w in wordDict:
      if s[index + 1 - len(w): index + 1] == w:
        if index + 1 - len(w) == 0:
          res += [w]
        else:
          prev = self.helper(source, index - len(w), wordDict)
          for p in prev:
            res.append(p + " " + w)

    self.memo[index] = res
    return res

