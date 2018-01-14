# 68_Text Justification
# 按照定义, 完成一行就确定一行.
# 每行, 比较当前行的总字符数 + 单词数(基本空格数) + 下一个单词.
# 如果超过规定, 下一个单词则应放在下一行, 本行补空格.(手动补)
# 利用循环剩余空格数i % len(curr) - 1, 每个单词后补空格. % len(curr) - 1是因为最后一个单词后面不能补空格, 所以总词数减一
# 最后一行手动添加, 循环结束后的最后一行, curr里是剩下的不超长度的单词组. 只用简单空格分隔后连接即可.

class Solution:
  def fullJustify(self, words, maxWidth):
    res, curr, charNum = [], [], 0
    for word in words:
      if charNum + len(curr) + len(word) > maxWidth:
        for spaceIndex in range(maxWidth - charNum):
          curr[spaceIndex % (len(curr) - 1 or 1)] += " "
        res.append("".join(curr))
        curr, charNum = [], 0
      curr.append(word)
      charNum += len(word)
    return res + [" ".join(curr).ljust(maxWidth)]
