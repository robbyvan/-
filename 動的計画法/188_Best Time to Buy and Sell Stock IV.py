# 188_Best Time to Buy and Sell Stock IV

class Solution:
  def wordBreak(self, s, wordDict):
    self.memo = {}
    return self.helper(s, len(s) - 1, wordDict)

  def helper(self, s, index, wordDict):
    if index in self.memo:
      return self.memo[index]
    ans = []
    for w in wordDict:
      if s[index + 1 - len(w): index + 1] == w:
        if index + 1 - len(w) == 0:
          ans += [w]
          print(ans)
        elif index + 1 - len(w) > 0:
          others = self.helper(s, index - len(w), wordDict)
          newAns = list(map(lambda item: item + " " + w, others))
          print(newAns)
          ans += newAns
    self.memo[index] = ans
    print("?")
    return ans

a = Solution().wordBreak("catsanddog", ["cat","cats","and","sand","dog"])
print(a)