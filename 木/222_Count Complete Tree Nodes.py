# 222_Count Complete Tree Nodes
# 完全二叉树, 只有最后一层不一定满.
# 递归比较左右高度. 
# 如果左的左高 > 右的左高 => 右是满二叉树
# 如果左的左高 == 右的左高 => 左是满二叉树
# 满二叉树节点总数: 2^h

class Solution:
  def countNodes(self, root):
    if not root:
      return 0
    lh = self.leftHeight(root.left)
    rh = self.leftHeight(root.right)
    if lh == rh:
      return pow(2, lh) + self.countNodes(root.right)
    return pow(2, rh) + self.countNodes(root.left)
  
  def leftHeight(self, node):
    if not node:
      return 0
    return 1 + self.leftHeight(node.left)