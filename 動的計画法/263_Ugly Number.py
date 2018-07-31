# 263_Ugly Number
# 顺序对2, 3, 5求余除法

class Solution:
  def isUgly(self, num):
    if num < 1:
      return False
    if num == 1:
      return True
    while num % 5 == 0:
      num = num / 5
    while num % 3 == 0:
      num = num / 3
    while num % 2 == 0:
      num = num / 2
    return num == 1

# class Solution:
#   def isUgly(self, num):
#     if num < 1:
#       return False
#     if num == 1:
#       return True
#     q = [2, 3, 5]
#     while q[0] <= num:
#       if num in q:
#         return True
#       nextQ = []
#       for key in q:
#         nextQ.extend([key * 2, key * 3, key *5])
#       q = nextQ
#     return False

# a = Solution().isUgly(244)
# print(a)
