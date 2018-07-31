# 199_Binary Tree Right Side View
# 直接BFS找每层最后一个结点即可.
# 或者DFS. 优先访问右子结点, 所以每层第一次遇见(if depth == len(res))的结点是该层的解.


class Solution:
  def rightSideView(self, root):
    res = []
    self.helper(root, 0, res)
    return res
  
  def helper(self, node, depth, res):
    if node is None:
      return
    if depth == len(res):
      res.append(node.val)
    self.helper(node.right, depth + 1, res)
    self.helper(node.left, depth + 1, res)

  # def rightSideView(self, root):
  #   res = []
  #   if not root:
  #     return res
  #   q = [root]
  #   while q:
  #     nextLevel, path = [], []
  #     for node in q:
  #       path.append(node.val)
  #       if node.left:
  #         nextLevel.append(node.left)
  #       if node.right:
  #         nextLevel.append(node.right)
  #     res.append(path[-1])
  #     q = nextLevel
  #   return res
