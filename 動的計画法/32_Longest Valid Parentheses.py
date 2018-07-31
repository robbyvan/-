# 32_Longest Valid Parentheses
# 见字符串32
# 当前长度 = ")"坐标 - 当前的左尽头, 同步更新maxLen.
# 左尽头有可能空或不空 => i - stack[-1]还是i - left + 1
# 左尽头有无offset(说明有断开) => 断开时更新left

class Solution:
  def longestValidParentheses(self, s):
    if not s:
      return 0
    maxLen, left, stack  = 0, 0, []
    for i, ch in enumerate(s):
      if ch == "(":
        stack.append(i)
      elif ch == ")":
        if not stack:
          left = i + 1
        else:
          stack.pop()
          if stack:
            maxLen = max(maxLen, i - stack[-1])
          else:
            maxLen = max(maxLen, i - left + 1)
    return maxLen