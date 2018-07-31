# 117_Populating Next Right Pointers in Each Node II

class Solution:
  def connect(self, root):
    tail, dummy = TreeLinkNode(0)
    while node:
      tail.next = node.left
      if tail.next:
        tail = tail.next
      tail.next = node.right
      if tail.next:
        tail = tail.next

  # def connect(self, root):
  #   q, lvl, curr = root, None, None
  #   while q:
  #     if q.left:
  #       if not lvl:
  #         lvl = curr = q.left
  #       else:
  #         curr.next = q.left
  #         curr = curr.next
  #     if q.right:
  #       if not lvl:
  #         lvl = curr = q.right
  #       else:
  #         curr.next = q.right
  #         curr = curr.next
  #     q = q.next
  #     if not q and lvl:
  #       q, lvl, curr = lvl, None, None