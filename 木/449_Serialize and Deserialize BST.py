# 449_Serialize and Deserialize BST
# 前序根左右生成data
# 解析利用deque, collections.deque(int(val) for val in data.split())
# 按顺序把deque内容依次(根左右)放在合适的位置.(利用build的min, max限制)
# 递归判定vals[0]是否在范围内, 成功 => val = vals.popleft()

class Codec:
  def serialize(self, root):
    vals = []
    def preOrder(node):
      if node:
        vals.append(node.val)
        preOrder(node.left)
        preOrder(node.right)
    preOrder(root)
    return " ".join(map(str, vals))

  def deserialize(self, data):
    vals = collections.deque(int(val) for val in data.split())

    def build(minVal, maxVal):
      if vals and minVal < vals[0] < maxVal:
        val = vals.popleft()
        node = TreeNode(val)
        node.left = build(minVal, val)
        node.right = build(val, maxVal)
        return node

    return build(float("-inf"), float("inf"))