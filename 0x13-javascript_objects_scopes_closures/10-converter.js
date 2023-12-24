#!/usr/bin/node

exports.converter = function (base) {

  function convert(arr) {
    let ans = 0;
    for (let i = arr.length - 1; i >= 0; i--) {
      ans = ans * 10 + arr[i]; 
    }
    return ans;
  }
  return function (val) {
    if (base !== 16) {
      let ans = [];
      while (val !== 0) {
        ans.push(val % base);
        val = Math.floor(val / base);
      }

      return convert(ans);
    } else {
      const res = {
        "10": 'a',
        "11": 'b',
        "12": 'c',
        "13": 'd',
        "14": 'e',
        "15": 'f'
      };
      let ans = "";
      while (val !== 0) {
        let temp = val % base;
        ans = (res[`${temp}`] ? res[`${temp}`]: temp) + ans;
        val = Math.floor(val / base);
      }
      return ans;
    }
  };
};
