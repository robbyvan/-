# 76_Minimum Window Substring
# 扫描一次
# 要在串s中找到串t的所有字母&相应个数的一部分
# 双指针i j, 指向头尾, 初始化0, 最佳指针I J
# 每每遇到一个新的字符, 改字符在hash表默认-1, 然后检查是否是需要的, 如果要[且还差!!], 才能counter - 1(counter用来确认是否找到了这样的子串)
# 然后检查counter.如果找到了满足的一个大串, 开始尽可能缩小这个串, 从头开始扔掉多余的字母, 找到最小的这样的串
# 比较当前解和保存的S[I:J], 如果更小, 就更新I, J
import collections
class Solution:
  def minWindow(self, s, t):
    need, missing = collections.Counter(t), len(t)
    left, optLeft, optRight = 0, 0, 0
    found = False
    for right, char in enumerate(s):
      if need[char] > 0:
        missing -= 1

      need[char] -= 1

      if missing <= 0:
        while left < right and need[s[left]] < 0:
          need[s[left]] += 1
          left += 1
        if not found or right - left <= optRight - optLeft:
          optLeft, optRight = left, right
        found = True        
    return s[optLeft:optRight + 1] if found else ""