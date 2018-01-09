# 385_Mini Parser
# 按照定义.利用stack.
# 当前操作的"[]"在stack顶端, 遇到"]"后, 如果stack还有, 则弹出, 并添加到上级[]
# 如果是数字:
# 第一次遇到数字, 记录开始坐标, 直到遇到非数字("]", ",")或者到了s末尾
# int(s[start:i+1])然后添加到stack顶端. (注意有可能纯数字, 则先创建一个NI进栈, 再添加数字进去)

class Solution:
  def deserialize(self, s):
    stack, start = [], -1
    for i, char in enumerate(s):
      if char == '[':
        stack.append(NestedInteger())
      elif char == ']':
        if len(stack) > 1:
          t = stack.pop()
          stack[-1].add(t)
      elif char.isdigit() or char == '-':
        if start == -1:
          start = i
        if i == len(s) - 1 or not s[i + 1].isdigit():
          if stack:
            stack[-1].add(NestedInteger(int(s[start: i + 1])))
          else:
            stack.append(NestedInteger(int(s[start:i + 1])))
          start = -1
    return stack.pop()

#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """