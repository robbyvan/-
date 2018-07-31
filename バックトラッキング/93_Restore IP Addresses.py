# 93_Restore IP Addresses
# 普通dfs. 限制条件: 段数等于4 => 判断是否是path, 段数不超过4 => 选择路径(要求不是0开头非零数, 且小于256)
# 注意选择的时候的去重: for right in range(min(3, len(source))) 要求个min, 否则cur = source[:right + 1]可能导致重复

class Solution:
  def restoreIpAddresses(self, s):
    res = []
    if len(s) > 12 or len(s) < 4:
      return res
    self.helper(s, 0, "", res)
    return res

  def helper(self, source, count, path, res):
    if count == 4:
      if not source:
        res.append(path[1:])
      return 

    for right in range(min(3, len(source))):
      cur = source[:right + 1]
      if cur and int(cur) < 256 and (not (cur[0] == "0" and len(cur) > 1)):
        self.helper(source[right + 1:], count + 1, path + "." + cur, res)

a = Solution().restoreIpAddresses("25525511135")
print(a)