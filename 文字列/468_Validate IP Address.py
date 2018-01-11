# 468_Validate IP Address
# 按照定义校验4, 6即可
# 注意re.split()时, 点"."要转义"\."

import re
class Solution:
  def validIPAddress(self, s):
    isIPv4 = self.checkIPv4(s)
    if isIPv4:
      return "IPv4"
    isIPv6 = self.checkIPv6(s)
    if isIPv6:
      return "IPv6"
    return "Neither"

  def checkIPv4(self, s):
    if "." not in s:
      return False
    ls = s.split(".")
    if len(ls) != 4:
      return False
    for item in ls:
      if (not item) or (not item.isdigit()) or(len(item) > 1 and item[0] == "0"):
        return False
      if int(item) > 255:
        return False
    return True

  def checkIPv6(self, s):
    d = "1234567890abcdefABCDEF"
    if ":" not in s:
      return False
    ls = s.split(":")
    if len(ls) != 8:
      return False
    for item in ls:
      if (not item) or len(item) > 4:
        return False
      for ch in item:
        if ch not in d:
          return False
    return True


