// 62_Unique Paths
// 空间复杂度: O(mn) => O(n): 只涉及两个行列的操作
// m * n => 两个row => 一个row, dp[j] = dp[j] + dp[j - 1]; j是上一行的内容, j - 1是本行的内容.

function uniquePaths(m, n) {
  let dp = [];
  for (let j = 0; j < n; ++j) {
    dp[j] = 1;
  }
  for (let i = 1; i < m; ++i) {
    for (let j = 1; j < n; ++j) {
      dp[j] = dp[j] + dp[j - 1];
    }
  }
  return dp[n - 1]
}

// function uniquePaths(m, n) {
//   let prev = [];
//   for (let j = 0; j < n; ++j) {
//     prev[j] = 1;
//   }
//   let cur = [];
//   for (let j = 0; j < n; ++j) {
//     cur[j] = 1;
//   }
//   for (let i = 1; i < m; ++i) {
//     for (let j = 1; j < n; ++j) {
//       cur[j] = cur[j - 1] + prev[j];
//     }
//     prev = cur.slice(0);
//     cur[0] = 1;
//   }
//   return cur[cur.length - 1];
// }

// function uniquePaths(m, n) {
//   const opt = [];
//   for (let i = 0; i < m; ++i) {
//     opt[i] = [];
//     for (let j = 0; j < n; ++j) {
//       opt[i][j] = 0;
//     }
//   }

//   for (let i = 0; i < m; ++i) {
//     opt[i][0] = 1;
//   }

//   for (let j = 0; j < n; ++j) {
//     opt[0][j] = 1;
//   }

//   for (let i = 1; i < m; ++i) {
//     for (let j = 1; j < n; ++j) {
//       opt[i][j] = opt[i - 1][j] + opt[i][j - 1];
//     }
//   }

//   return opt[m - 1][n - 1];
// }