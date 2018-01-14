# 127_Word Ladder
# 双向BFS
# 从头开始, 对每个单词的每一位进行变化, 变化后如果有满足的, 返回结果
# 否则检查变化后的单词, 是否合法(在wordList里面), 合法的单词作为下次的一个box, 并且从wordList里删掉该词
# 删掉: 已经用过了这个词, 后续如果再变成这个单词, 则重复运算了.
# 比较front, back大小, 选择小的进行后续的变换.
# 注意set([beginWord]), set(beginWord), { beginWord }

class Solution:
  def ladderLength(self, beginWord, endWord, wordList):
    if endWord not in wordList:
      return 0
    front, back, wordList = set([beginWord]), set([endWord]), set(wordList)
    wordLen = len(beginWord)
    step = 1
    while front:
      step += 1
      nextFront = set()
      for word in front:
        for i in range(wordLen):
          for c in string.lowercase:
            if c != word[i]:
              newWord = word[:i] + c + word[i+1:]
              if newWord in back:
                return step
              if newWord in wordList:
                nextFront.add(newWord)
                wordList.remove(newWord)
      front = nextFront
      if len(front) > len(back):
        front, back = back, front
    return 0

