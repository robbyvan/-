# 126_Word Ladder II
# 和127相同的解法, 但是每次变换成新词, 都要生成一条path, 把新词添进去.
# 注意append的内容, 如果里面已经是list了, 拼接还是list
# 如果里面是初始的一个词, 那么加上front[beginWord].append([beginWord])
# 多重循环的append, 可以写成单行的extend. 例如用 nextSet[nextWord].extend([path + [nextWord] for path in paths])替换
# for path in paths:
#   nextFront[newWord].append(path + [newWord])

import collections
class Solution:
  def findLadders(self, beginWord, endWord, wordList):
    res = []
    if endWord not in wordList:
      return res
    front, back = collections.defaultdict(list), collections.defaultdict(list)
    front[beginWord].append([beginWord])
    back[endWord].append([endWord])
    wordList = set(wordList)
    wordLen = len(beginWord)
    wordList.discard(start)
    foward = True
    while front:
      nextFront = collections.defaultdict(list)
      for word, paths in front.items():
        for i in range(wordLen):
          for ch in string.lowercase:
            if ch != word[i]:
              newWord = word[:i] + ch + word[i+1:]
              if newWord in wordList:
                for path in paths:
                  if foward:
                    nextFront[newWord].append(path + [newWord])
                  else:
                    nextFront[newWord].append([newWord] + path)
      front = nextFront

      common = set(front) & set(back)
      if common:
        if not foward:
          front, back = back, front
        for word in common:
          for head in front[word]:
            for tail in back[word]:
              res.append(head + tail[1:])
        return res

      if len(front) > len(back):
        front, back = back, front
        foward = not foward
      wordList -= set(front)
    return res
