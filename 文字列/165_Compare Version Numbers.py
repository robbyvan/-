# 165_Compare Version Numbers
# 1) 利用split分开"." => 两个字符数组
# 2) 删掉无用的后缀0.使用int()强转
# 3) 首先比较公共长度部分, int()比较, 返回-1或者1
# 4) 继续比较长度, 长的大, 短的小

class Solution(object):
  def compareVersion(self, v1, v2):
    version1 = self.trimRightZero(list(map(lambda x: int(x), v1.split('.'))))
    version2 = self.trimRightZero(list(map(lambda x: int(x), v2.split('.'))))

    for i in range(min(len(version1), len(version2))):
      if int(version1[i] > version2[i]):
        return 1
      elif int(version1[i] < version2[i]):
        return -1

    if len(version1) > len(version2):
      return 1
    elif len(version1) < len(version2):
      return -1
    else:
      return 0

  def trimRightZero(self, s):
    if len(s) == 0:
      return s
    while s[-1] == 0:
      s = s[0:-1]
      if len(s) == 0:
        break
    return s

