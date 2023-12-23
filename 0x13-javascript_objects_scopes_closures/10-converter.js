#!/usr/bin/node

exports.converter = function (base) {
  return function (val) {
    if (val !== 16) {
      let ans = 0;
      while (val !== 0) {
        ans = (ans * 10) + (val % base);
        val = Math.floor(val / base);
      }

      return ans;
    } else {
      const res = {
        10: 'a',
        11: 'c'

      };
      let ans = 0;
      while (val !== 0) {
        ans = (ans * 10) + (val % base);
        val = Math.floor(val / base);
      }
    }
  };
};
