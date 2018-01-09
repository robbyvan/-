# 32_Longest Valid Parentheses
# ")"一定出现在"("的右边才是合法的.
# 对于"(", 遇到就进栈
# 对于")", 遇到先看栈
# 如果空栈, 说明")"不合理, 扔掉, 更新left
# 如果不空, 就弹出一个, 然后更新count.
# 此时有两种情况, 第一种是直到当前段头都是合法的.比如()(), 所以直接i - left + 1
# 也有可能是比如((())), 此时对于第一个")"仅仅有1个括号匹配, 因此是i - (stack[-1] + 1) + 1

class Solution(object):
  def longestValidParentheses(self, s):
    count, left, stack = 0, 0, []
    for i, item in enumerate(s):
      if item == "(":
        stack.append(i)
      else:
        if len(stack) == 0:
          left = i + 1
          continue
        else:
          stack.pop()
          if len(stack) == 0:
            count = max(count, i - left + 1)
          else:
            count = max(count, i - stack[-1])
    return count