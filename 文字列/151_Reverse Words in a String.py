# 151_Reverse Words in a String
# 先翻转整个串, 然后翻转每个单词.
# 遇到一个非空字符, 并且这之前是空格(说明是一个新词开始), 且已有缓存词了, 那么把之前的词添加进结果, 然后修改缓存word
# 否则这个非空字符是词的继续, 接在word之前(翻转)
class Solution:
  def reverseWords(self, s):
    word = ""
    words = ""
    s = s[::-1]
    for i, char in enumerate(s):
      if (not char.isspace() and s[i - 1].isspace()) and word:
        words = words + word + ' '
        word = char
      elif not char.isspace():
        word = char + word
    words =  words + word
    return words
