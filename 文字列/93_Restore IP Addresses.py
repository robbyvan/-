# 93_Restore IP Addresses
# 寻找路径类型. 利用helper
# 目的: 4段
# 如果4段且用完, 记录并返回
# 如果超过4段, 返回
# 小于4段: 
# 如果没ip了, 返回
# 分别组成1, 2, 3位的数字
# 如果头0且不是单0, 或者超过了255, 返回
# 否则拼接path + s, 如果是不是最后一段, 补'.'否则不补

class Solution:
  def restoreIpAddresses(self, s):
    if len(s) > 12 or len(s) < 4:
      return []
    res = []
    self.helper(s, 0, "", res)
    return res

  def helper(self, ip, count, path, res):
    if count > 4:
      return
    if count == 4 and not ip:
      res.append(path)
      return
    for offset in range(1, 4):
      if offset > len(ip):
        return
      s = ip[:offset]
      if (s and s[0] == '0' and len(s) > 1) or int(s) > 255:
        return
      nextPath = path + s + '.' if count < 3 else path + s
      self.helper(ip[offset:], count + 1, nextPath, res)