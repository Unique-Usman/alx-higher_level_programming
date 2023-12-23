#!/usr/bin/node

module.exports.nbOccurences = function (arr, ele) {
  let count = 0;
  for (let i = 0; i < arr.length; i++) {
    if (ele === arr[i]) { count++; }
  }

  return count;
};
