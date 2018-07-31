# 297_Serialize and Deserialize Binary Tree
# 前序遍历, "根左右". 按顺序遍历生成字符串, 用","分割, 用"None"代替None
# 恢复: 按","split, 重新"根左右"顺序构造一棵树

class Codec:
  def serialize(self, root):
    pre = ""
    if not root:
      pre += ",None"
      return pre
    pre += "," + str(root.val)
    pre += self.serialize(root.left)
    pre += self.serialize(root.right)
    return pre
   
  def deserialize(self, encodeData):
    data = encodeData[1:].split(",")
    for i in range(len(data)):
      if data[i] == "None":
        data[i] = None
      else:
        data[i] = int(data[i])
    pos = -1
    root, count = self.buildTree(data, pos)
    return root
  
  def buildTree(self, data, pos):
    pos += 1
    if pos >= len(data) or data[pos] == None:
      return None, pos
    root = TreeNode(data[pos])
    root.left, pos = self.buildTree(data, pos)
    root.right, pos = self.buildTree(data, pos)
    return root, pos

  