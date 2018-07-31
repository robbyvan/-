# 466_Count The Repetitions

class Solution:
  def getMaxRepetitions(self, s1, n1, s2, n2):
    start = {}
    s1Round, s2Round, s2Index = 0, 0, 0
    while s1Round < n1:
      s1Round += 1
      for ch in s1:
        if ch == s2[s2Index]:
          s2Index += 1
          if s2Index == len(s2):
            s2Round += 1
            s2Index = 0
      if s2Index in start:
        prevS1Round, prevS2Round = start[s2Index]
        circleS1Round, circleS2Round = s1Round - prevS1Round, s2Round - prevS2Round
        res = (n1 - prevS1Round) / circleS1Round * circleS2Round
        leftS1Round = (n1 - prevS1Round) % circleS1Round + prevS1Round
        for key, val in start.iteritems():
          if val[0] == leftS1Round:
            res += val[1]
            break
        return res / n2
      else:
        start[s2Index] = (s1Round, s2Round)
    return s2Round / n2