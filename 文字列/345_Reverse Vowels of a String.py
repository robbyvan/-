# 345_Reverse Vowels of a String
# 双指针: 只有都指向aeiou才交换. (while + 3 if)

class Solution:
  def reverseVowels(self, s):
    d = "aeiouAEIOU"
    arr = list(s)
    l, r = 0, len(arr) - 1
    while l < r:
      if arr[l] in d and arr[r] in d:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
      if s[l] not in d:
        l += 1
      if s[r] not in d:
        r -= 1
    return "".join(arr)