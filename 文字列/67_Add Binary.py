# 67_Add Binary
# 递归, 所有情况:
# 1.有空字符串 => 返回对面
# 2."0" + "0" => 该位"0", 相加之前
# 3. "0" + "1" => 该位"1", 相加之前
# 4. "1" + "1" => 该位"0", 结果再和"1"相加

class Solution:
  def addBinary(self, a, b):
    if len(a) == 0:
      return b
    if len(b) == 0:
      return a
    if a[-1] == "1" and b[-1] == "1":
      return self.addBinary(self.addBinary(a[:-1], b[:-1]), "1") + "0"
    if a[-1] == "0" and b[-1] == "0":
      return self.addBinary(self.addBinary[:-1], b[:-1]) + "0"
    return self.addBinary(a[:-1], b[:-1]) + "1"