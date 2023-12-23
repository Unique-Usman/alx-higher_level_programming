#!/usr/bin/node

module.exports.logMe = (function () {
  let count = 0;
  return function (arg) {
    console.log(`${count}: ${arg}`);
    count++;
  };
})();
