# 58_Length of Last Word
# 按照定义. 从末尾向前.
# 先删除掉" ", 然后统计非空格次数
class Solution:
  def lengthOfLastWord(self, s):
    if not s or len(s) == 0:
      return 0
    wordLen, tail = 0, len(s) - 1
    while tail >= 0 and s[tail] == " ":
      tail -= 1
    while tail >= 0 and s[tail] != " ":
      wordLen += 1
      tail -= 1
    return wordLen

