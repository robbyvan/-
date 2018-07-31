// 264_Ugly Number II
// 

function nthUglyNumber(n) {
  const res = [1];
  let i2 = 0, i3 = 0, i5 = 0;
  while (res.length < n) {
    let nextUgly = Math.min(res[i2] * 2, res[i3] * 3, res[i5] * 5);
    if (nextUgly === res[i2] * 2) {
      i2 += 1;
    } else if (nextUgly === res[i3] * 3) {
      i3 += 1;
    }else if (nextUgly === res[i5] * 5) {
      i5 += 1;
    }
    res.push(nextUgly);
  }
  return res[res.length - 1];
}
