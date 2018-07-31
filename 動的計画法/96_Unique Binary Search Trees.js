// 96_Unique Binary Search Trees
// 求n => 考虑规模为i的问题, opt[i] = opt[k] * opt[i - k] { for all possible cut k }

function numTrees(n) {
  if (n === 0 || n === 1) {
    return 1;
  }
  const dp = [1, 1];
  for (let i = 2; i <= n; ++i) {
    dp[i] = 0;
    for (let k = 1; k <= i; ++k) {
      dp[i] = dp[i] + dp[k - 1] * dp[i - k];
    }
  }
  return dp[n];
}