# 344_Reverse String
# 双指针
# 递归: return self.reverseString(s[l/2:]) + self.reverseString(s[:l/2])

class Solution:
  def reverseString(self,s):
    arr = list(s)
    l, r = 0, len(s) - 1
    while l < r:
      arr[l], arr[r] = arr[r], arr[l]
      l += 1
      r -= 1
    return "".join(arr)