# 126_Word Ladder II
# 双向BFS, 与之前不同的是, 需要返回所有的最短解 => 在某层找到一个新词时候不再检查(newWord in back => 是一个答案) => 而是完成了这一层的构造后统一检查该层
# 同时因为求路径, 到达每层的词可能有多种方式, 因此存储方式是dict{word: paths[]
# 检查结束条件: 新的front和back具有相同的key
# 构造路径 => front[common] + back[common][1:]

class Solution:
  def findLadders(self, beginWord, endWord, wordList):
    if endWord not in wordList:
      return []
    front, back = collections.defaultdict(list), collections.defaultdict(list)
    wordList = set(wordList)
    wordLen = len(beginWord)
    wordList = wordList - set([beginWord])
    front[beginWord] += [[beginWord]]
    back[endWord] += [[endWord]]

    foward = True
    res = []
    while front:
      nextFront = collections.defaultdict(list)
      for word, paths in front.items():
        for i in range(wordLen):
          for sub in string.lowercase:
            if sub == word[i]:
              continue
            newWord = word[:i] + sub + word[i + 1:]
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

      wordList = wordList - set(front)
    return res

