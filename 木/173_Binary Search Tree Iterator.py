# 173_Binary Search Tree Iterator
# next() and hasNext() should run in average O(1) time and uses O(h) memory
# mem只能O(h), 每层只能存一个点, 那么就存最左
# hasNext()检查栈是否空
# 取next(), 因为BST是左 < 中 < 右, 取出一个节点后, 下一个就是其右孩子的最左, 依次每层左进栈即可.

class BSTIterator:
  def __init__(self, root):
    self.stack = []
    while root:
      self.stack.append(root)
      root = root.left

  def hasNext(self):
    return len(self.stack) > 0

  def next(self):
    node = self.stack.pop()
    x = node.right
    while x:
      self.stack.append(x)
      x = x.left
    return node.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())