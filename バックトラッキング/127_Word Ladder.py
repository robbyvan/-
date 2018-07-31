# 127_Word Ladder
# 双向BFS. 从front出发, 找到所有的变换组成下一层.(找: 对每个词的每一位(2重), 分别替换成不为该位本身的另一个字符(1重), 和目的back比较 => return? => 是否合法?)

class Solution:
  def ladderLength(self, beginWord, endWord, wordList):
    if endWord not in wordList:
      return 0
    front, back, wordList = set([beginWord]), set([endWord]), set(wordList)
    wordList = wordList - front
    wordLen = len(beginWord)
    count = 1
    while front:
      count += 1
      nextFront = set()
      for f in front:
        # for each word "f" in front, check all possible jump
        for i in range(wordLen):
          for ch in string.lowercase:
            if ch != f[i]:
              newWord = f[:i] + ch + f[i + 1:]
              if newWord in back:
                return count
              if newWord in wordList:
                wordList.remove(newWord)
                nextFront.add(newWord)
      front = nextFront
      if len(front) > len(back):
        front, back = back, front
    return 0
