# 125_Valid Palindrome
# 双指针 while + 3 if

class Solution:
  def isPalindrome(self, s):
    l, r = 0, len(s) - 1
    while l < r:
      if not s[l].isalnum():
        l += 1
        continue
      if not s[r].isalnum():
        r -= 1
        continue
      if s[l].lower() != s[r].lower():
        return False
      l += 1
      r -= 1
    return True