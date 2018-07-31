// 95_Unique Binary Search Trees II
// DFS: 对于1~n, 当所有的i为根时, 左子树[1, i-1], 右子树[i + 1, n]
// 基本: start > end => null; start === end => TreeNode(start)

function generateTrees(n) {
  if (n === 0) {
    return [];
  }
  return helper(1, n);
}

function helper(start, end) {
  const res = [];
  if (start > end) {
    res.push(null);
    return res;
  }
  if (start === end) {
    res.push(new TreeNode(start));
    return res;
  }
  for (let i = start; i <= end; ++i) {
    const left = helper(start, i - 1);
    const right = helper(i + 1, end);
    for (let lnode of left) {
      for (let rnode of right) {
        const root = new TreeNode(i);
        root.left = lnode;
        root.right = rnode;
        res.push(root);
      }
    }
  }
  return res;
}