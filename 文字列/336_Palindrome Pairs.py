# 336_Palindrome Pairs
# 回文的几种组合
# 任意回文 + "" ; "" + 任意回文
# 任意串 + 逆串
# 逆乱序 + [部分回文+乱序]; [乱序 + 部分回文] + 逆乱序
# 利用d保存初次扫描的(key, val), 然后根据要求寻找即可
class Solution:
  def palindromePairs(self, words):
    res = []
    if not words:
      return res

    d = {}
    for i, word in enumerate(words):
      d[word] = i

    if "" in d:
      for i, word in enumerate(words):
        if self.isPalindrome(word) and word != "":
          res.append([d[""], i])
          res.append([i, d[""]])

    for i, word in enumerate(words):
      rWord = word[::-1]
      if rWord in d and d[rWord] != i:
        res.append([i, d[rWord]])

    for i, word in enumerate(words):
      for cut in range(1, len(word)):
        if self.isPalindrome(word[:cut]):
          rWord = word[cut:][::-1]
          if rWord in d and d[rWord] != i:
            res.append([d[rWord], i])

        if self.isPalindrome(word[cut:]):
          rWord = word[:cut][::-1]
          if rWord in d and d[rWord] != i:
            res.append([i, d[rWord]])
    return res

  def isPalindrome(self, s):
    i, j = 0, len(s) - 1
    while i < j:
      if s[i] != s[j]:
        return False
      i += 1
      j -= 1
    return True