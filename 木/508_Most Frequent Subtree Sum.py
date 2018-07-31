# 508_Most Frequent Subtree Sum
# 遍历一次, 其间利用hash表保存结果. 最后取出最大的几项即可

class Solution:
  def findFrequentTreeSum(self, root):
    if not root:
      return []
    d = collections.Counter()
    self.subSum(root, d)
    maxFrq = max(v for v in d.values())
    res = []
    for k in d.keys():
      if d[k] == maxFrq:
        res.append(k)
    return res

  def subSum(self, node, d):
    if not node:
      return 0
    left = self.subSum(node.left, d)
    right = self.subSum(node.right, d)
    val = left + right + node.val
    d[val] += 1
    return val