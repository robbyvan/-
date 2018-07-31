# 72_Edit Distance
# 见字符串72

class Solution:
  def minDistance(self, word1, word2):
    m, n = len(word1), len(word2)
    opt = [[0] * (n + 1) for _ in range(m + 1)]

    for j in range(n + 1):
      opt[0][j] = j
    for i in range(m + 1):
      opt[i][0] = i

    for i in range(m):
      for j in range(n):
        if word1[i] == word2[j]:
          opt[i + 1][j + 1] = opt[i][j]
        else:
          opt[i + 1][j + 1] = min(
            opt[i + 1][j],
            opt[i][j],
            opt[i][j + 1]
          ) + 1

    return opt[-1][-1]
